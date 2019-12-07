# remote-controlled-clj


## TODO

These are the features required:
- [ ] Be able to create an empty simulation space - an empty 50 x 50 grid;
- [ ] Be able to create a robot in a certain position and facing direction;
- [ ] Be able to create a dinosaur in a certain position;

- [ ] Issue instructions to a robot - a robot can turn left, turn right, move forward, move backwards, and attack;
- [ ] A robot attack destroys dinosaurs around it (in front, to the left, to the right or behind);

- [ ] No need to worry about the dinosaurs - dinosaurs don't move;
- [ ] Display the simulation's current state;

- [ ] Two or more entities (robots or dinosaurs) cannot occupy the same position;
- [ ] Attempting to move a robot outside the simulation space is an invalid operation.

## Architecture

The API is  written in clojure based on Hexagonal Architecture, for managing the life-cycle
of components which have run-time state, also can be seen as the dependency injection for
immutable data structures.

### Ports

### Adpaters

### Controllers

### Logic


## License

Copyright © 2019 FIXME

This program and the accompanying materials are made available under the
terms of the Eclipse Public License 2.0 which is available at
http://www.eclipse.org/legal/epl-2.0.

This Source Code may also be made available under the following Secondary
Licenses when the conditions for such availability set forth in the Eclipse
Public License, v. 2.0 are satisfied: GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or (at your
option) any later version, with the GNU Classpath Exception which is available
at https://www.gnu.org/software/classpath/license.html.
