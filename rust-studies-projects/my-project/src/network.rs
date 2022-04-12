
/* Socket
 Network endpoint, TCP socket
 Socket should be managed similiar memory and socket problems

Memory
- Use after free
- Double free
- Memory leaks
- Mitigated with garbage collection
- Mitigated with ownership!

Sockets
- Use after close
- Closing twice
- Socket leaks
- Not mitigated with garbage collection
- Mitigated with ownership!


//Mutex<T> (Mutual Exclusion)

Only let one thread at a time change the inner value
To modify the value, acquire the mutex lock
Release the lock after modifying to let other threads acquire the lock
Owner goint out of scope = lock released!

Rc<T> (Reference Counted)
Allows for multiple owners
Keeps track of how many owners exist
Memory is cleaned up when the last owner goes out of scope
Count management happen automatically when each owner goes out of scope

in this module Ownership of More tahn Memory
management of sockets
otehr resources managed with ownership
customizing types with the drop trait

The Drop Trait
One method: drop
drop takes &mut self
*/

use std::thread;
use std::time::Duration;
use std::net::TcpListener;

fn open_socket_for_five_seconds() {
    let _listener = TcpListener::bind("127.0.0.1:5000").unwrap();
    thread::sleep(Duration::from_secs(5));
}

fn exec_socket() {
    open_socket_for_five_seconds();
    println!("Back in main");
    thread::sleep(Duration::from_secs(5));
}

struct Noisy {
   id: i32,
}

impl Drop for Noisy {
    fn drop(&mut self) {
        println!("Noisy number {} going out of scope!", self.id);
    }
}

fn main() {
    let _n1 = Noisy { id: 1 };
    let _n2 = Noisy { id: 2 };
    println!("Ended");
}
