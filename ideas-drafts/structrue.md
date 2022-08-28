# Patchforge's suggested architecture

A high focus on separating infrastructure from core code.
See hexagonal architecture or, better yet, "Functional core, imperative shell"

## High level overview

### Infrastructure

Each major component is given its own namespace. It has all the things
needed for itself to work.

    patchforge/
        web/
            ...
        db/
            ...
        git/
            ...
        sshd/
            ...

Most of these are self-explanatory. `db` is given this name because
patchforge deals with git _repositories_, so to avoid confusion with
the term, `db` as database access is the chosen name instead.

In there we will have implementation for db protocols:

    patchforge/
        db/
            accounts.clj
            repositories.clj
            ...

### Components

Wiring of components is done at the highest level on `patchfoge.components`.
Each infrastructure module should have a compnents file as well, somewhat like so:

    patchforge/
        components.clj  ;; high level, orchestrates everything
        web/
            components.clj  ;; defines the web components only
        db/
            components.clj  ;; only db access components
        git/
            compoennts.clj
        ...

I enjoyed using weavejester/integrant for this. In fact, I have a working
integrant setup with config and db datasource using next-jdbc that
we can reuse.

### The domain

Code is organized in bounded contexts. As of now, I have identified four:

- accounts (organizations, users, groups)
- repositories (git repos, permissions, changes)
- reviews (review score, comments made, etc.)
- notifications (notification preferences etc.)

The domain architecture bundles code by functionality first, like so:

    patchforge/
        domain/
            use_cases/
                accounts.clj
                repositories.clj
                ...
            entities/  ;; or models
                accounts.clj
                repositories.clj
                ...
            logic/
                accounts.clj
                ...
            protocols/
                accounts.clj
                ...

#### `patchforge.domain.use-cases.*`

Each use-case file contains functions for each use-case. For example,
for an hypothetical `create-user` use-case, we would have:

    (s/defn create-user
      [email :- s/Str
       password :- s/Str
       as-of :- datetime-etc
       {db :accounts-db
        events :accounts-events}]
        ...)

The last element of the function is a components map for dependency
injection. We only interact with data from this map through protocols.
So, for the example above in an use-case `use-cases.accounts/create-user`,
we would use `(protocols.accounts/create-user db ...)`, for example.
Same for the events, `(protocols.accounts/user-created events ...)`
so we can let event handling to happen up top.

### `patchforge.domain.entities.*`

Mostly plumatic/schema definitions. These are used mostly everywhere.

Care must be taken with regards to value objects or DTOs. I prefer
domain entities to have strong constraints. Sometimes what we need
is a DTO, not a weaker domain model.

### `patchforge.domain.logic.*`

All IMMUTABLE, PURE functions regarding this bounded context.

It may use lbirary code if and only if the library code
being used is itself pure. A prime counter-example
is password hashing: it is inherently impure, so it
should not be done directly from logic code.

### `patchforge.domain.protocols.*`

Defines the protocols _needed by_ the bounded context, i.e.
they must be provided for the context to do its thing.

It is here where we define protocols for db access,
repository handling, events and more.

## Cross-boundaries code

This is a tricky one that needs more research. Ideally, I would
like to avoid invoking any code that doesn't belong in the
bounded context itself. That is, if `use-cases.accounts`
invokes code from `logic.repositories`, for example, that
should be considered a code smell.

But Patchforge should be designed as a monolith, so we would
rather not have to deal with microservices and such, as well
as leveraging a few powers monoliths allow, like easier
transaction handling.

Therefore, whenever we need to have cross-context code,
there are two ways of adding decoupling without adding
too much complexity, hopefully.

This is an idea, anyway.

### Synchronous operations

When a context needs to fetch data from another, it should
do so through a component. This is to enforce separation
of concerns. So imagine that, for some reason, `use-cases.repositories`
needs access to user data that belongs to accounts.
It should, then, describe a gateway for it, like so:

    patchforge/
        domain/
            protocols/
                repositories.clj  ;; here `protocol AccountsGateway` is defined

Then the components map should receive `accounts-gateway` as one
of its components. The idea here is to abstract away what could
have been an http call, for example.

Then, the implementation is done through a component:

    patchforge/
        domain/
            components/
                accounts.clj  ;; imports and implements AccountsGateway protocol

Then this should be wired through `patchforge.components` like any other.

HOWEVER. As per DDD states, usually bounded contexts should have
all the data it needs to function, but not more. So these should
be somewhat rare.

For example, both `entities.accounts` and `entities.repositories` have
the `User` entity. They are treated differently inside the domain
mainly to isolate the bounded contexts, since `entities.repositories/User`
is a different facet of User that may or may not have the same attributes.
THese do not, necessarily, map to separate tables on the database.
Domain entities do not always map directly to database tables, so
keep that in mind.

### Asynchronous operations

Now here are the usual events after something happens. For example,
once a Change Request is created, usually the author themselves
should be subscribed to it to receive new notifications.
So in `use-cases.repositories/new-change` (for example), it would
invoke `(protocols.repositories/change-created events change)`
with the intent of propagating the event... but the handling
of notifications should be on `notifications`, not `repositories`.

Now here is the kicker: ideally, we want to handle both `repositories`
and `notifications` code without having to rely on a message queue,
if only to reduce complexity. Keeping as most as possible in a
single database transaction is nice as well.

So whichever component implements `protocols.repositories/change-created`
may decide to handle immediately. This is transparent to the use-case,
handling the event synchronously is an implementation detail.
Somewhat like so:

    patchforge/
        events/
            repositories.clj  ;; implements protocols.repositories/change-created
            producer.clj      ;; in case we do want to produce messages to a message queue
            consumer.clj      ;; counterpart to producer

So in `events.repositories`, we could have one of two things:

a) a function that invokes the producer so that the message is put on a message queue

    (change-created [_this change]
        (producer/change-created redis change))

b) a function that immediately invokes the relevant use-case so that it is handled immediately:

    (change-created [_this change]
        (consumer/change-created change components))

The implementation details for this are still being considered.
I want something that is _very_ lightweight, but still allows
for events to be chosen to be handled synchronously to take
advantage of the database.

## Testing

This is something I'm figuring out, but I have a few ideas.
STILL UNDECIDED. I'm considering
the following hierarchy:

### Unit tests

No brainer. All tests under `domain.logic` are unit tests.

I wonder, code for a few things like git manipulation
could also have "unit" tests too, for the only reason
that we're testing the unit itself: the git component,
the database query, so on and so forth.

### Integration tests

These have two flavors: testing use-cases directly by stubbing out
dependencies, and testing API responses.

I feel like testing API responses (i.e. asserting that it returns 
a certain status code and etc.) is more useful for public APIs,
which should be a concern later.

There isn't always a 1-1 correspondence between the public API
and the webapp API, so the HTTP-aware integration test should
be the only one testing http statuses and responses.

Even though we're still stubbing stuff out here, it should
be noted that use-cases are through and through "shell code",
i.e. they are fully imperative. We are asserting that the
use cases are orchestrating the components correctly,
which I feel is the integration test's domain.

### Functional tests

Nothing, or very, _VERY_ little, is stubbed out here. Real
server, real database, real mail server, real message queue.

These are written in BDD style (though we don't need a BDD
test framework) and could use selenium so that we tie together
back-end and front-end. These, too, don't check for http
status codes, because that is an implementation detail.

### Problems

I'm still on the fence about the gap between integration
and functional tests. Generally I believe that integration
tests should use real components as much as possible...

If we do integration tests with real database and whatnot,
we still need to verify that the components have had
state changes afterwards. I would rather not do that
through wonky intermediary functions that reimplement production
code in tests, and I usually don't like spies either.
So stubbing out dependencies for use-cases tests seem
like a fair compromise, while public API integration
tests use more components because we need it to be
more stable. Leaving gaps in tests that are expected
to be exercised/picked on functional tests seems like
a good idea to be, because we're not testing implementation
details anymore just as long as the whole works... but I'm 
not sure. Still thinking this one through, so for now
this is undecided.

https://gist.github.com/lsmag/e8b9e5d166eedd121a78e85007ac45b4
https://elixirschool.com/en/lessons/basics/control_structures#with-3
https://git.sr.ht/~sampsm/match-with
