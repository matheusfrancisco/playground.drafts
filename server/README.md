# Anki application


## Stack

- Datomic
- Clojure
- Clojurescript
- Re-frame
- Datascript (via Re-Posh)


# Info Model

## User
- id           (uuid)
- full-name    (string)
- username     (string)
- email        (string => unique)
- password     (string => unique)
- token        (string)


## Topics
- id              (uuid)
- author       (Ref)
- title        (string)
- tags         (vector of strings)


## Cards
- id              (uuid)
- topic           (Ref)
- front           (string)
- back            (string)
- progress        (long)
- next-study-date (date|instant)


## HTTP Rest Points

## Auth
/api/login
- POST => login a user
/api/register
- register a user

## Users
/api/users/:user-id
- GET       => get a single user by ID
- PUT       => update a user
- DELETE    => Delete a single user


/api/users
- POST => Post a new user


## Users
/api/users/:user-id/decks/:decks-id
- GET       => get a single deck by ID beloging to a certain user
- PUT       => update a deck
- DELETE    => Delete a deck

/api/users/:user-id/decks
- POST => Post a new deck

## Cards
/api/users/:user-id/decks/:deck-id/cards/:card-id
- GET      => get a single cards by ID belonging to a certain deck
- PUT      => update a card
- DELETE   => delete a card

/api/users/:user-id/decks/:deck-id/cards
- POST => Post a new card


