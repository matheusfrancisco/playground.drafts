use std::io;
/*
 fn name(param1: type1, ...) -> retrun_type {
    ...body...
 }
 * */

fn next_bday(name: &str, current_age: u8) {
    let next_age = current_age + 1;
    println!("Hi, {}, on your next bday you ´ll be {}! ", name, next_age);
}

fn square(num: i32) -> i32 {
    num * num
}

fn _main() {
    println!("Hello, world!");
    // all variables declarete start with let

    let x = 5;
    let y = 1;
    let z = x + y;

    println!("z is {}", z);

    // rust is immutable by default
    /*
    let k = 1;
    k += 1;
     * */
    // to create mutate var
    let mut k = 1;
    k += 1;

    println!("k is {}", k);

    //all variables in rust has a type TypeName = i32;
    // let x = true it is boolean
    // let x: i36 = 1;

    //core types
    //Boolean it is call bool (True or False)

    let a = true;
    let b = false;
    if a {
       println!("a it is true")
    }

    if !b {
        println!("b is false")
    }

    // Integer Types
    // signed and unsigned
    // i8    u8
    // i16   u16
    // i32   u32
    // i64   u64

    // if we use i8
    // 8bits [+/- , 0/1, 0/1, 0/1, 0/1, 0/1, 0/1, 0/1]
    // -128 --- 128
    // u8 use 0 or positives
    // [0/1, 0/1, 0/1, 0/1, 0/1, 0/1, 0/1]
    // 0 -> 255 because not uses signed it has more numbers
    //
    // More Interger Types
    // isize and usize
    // Architecture dependent pointer size
    // used for indexes, counts

    let a = [100, 200, 300];
    let _b = a[0] ; //0 is isize

    // Floating point nubmers
    // default f64 because it is more precision
    let _a = 54.6;

    // Char
    let _c = 'a';
    // it is different from strings which uses double ""
    //
    // Tuples
    // Group multiple values into one type
    // Dont have to be the same type
    let tup = (1, 'c', true);
    let first = tup.0;
    let second = tup.1;

    println!("{}", first);
    println!("{}", second);

    // also we could destructuring things
    let (_y, _z, _w) = tup;
    println!("{},  {}, {}", _y, _z, _w);

    //Array
    //all elments should have same type
    let mut b = [1, 2, 3];
    b[0] = 0;
    // print the array after change it
    println!("{:?}", b);

    //Slices reference to a contiguous subset of data in another data structure
    let _b  = &a[0..1];
    println!("{:?}", _b);

    next_bday("xico", 2)

}

fn _flow() {
    //Control flow features

    /*
     *
     if expression {
        ... code
     } else if expression {
        ... code
     } else {
        ... code
     }
     * */
    let num = 10;
    let discount  =  if num % 2 == 0 {
        50
    } else {
        10
    };
    println!("Your discount is {}!", discount);

    //loop {  } while run forever until break
    loop {
        println!("What is the secret?");
        let mut word = String::new();
        io::stdin().read_line(&mut word).expect("Failed to read line");

        if word.trim() == "rust" {
            break;
        }
    }
    println!("Yeaaahh");

    // while expression { ...code } it will run until the expression be true
    let mut word = String::new();
    while word.trim() == "rust"  {
        println!("What is the secret?");
        io::stdin().read_line(&mut word).expect("Failed to read line");
    }

    // for x in items {}
    //  for item in colletion { ... code }
    //
    for i in 1..11 {
        println!("Number {}", i);
    }

    // match
    let _x = 3;
    match _x {
        1 => println!("One"),
        2 => println!("Doesnt match"),
        3 => println!("Threeeeee"),
        _ => println!("catch"),
    }

    let _p1 = 3;
    let _p2 = 2;

    match (_p1, _p2) {
        (1, 1) => println!("One"),
        (1, 2) => println!("Letssss bora"),
        (_, 2) | (2, _) =>  {
            println!("At least one is two");
        },
        _ => println!("catch"),
    }

    let _p1 = 1;
    let _p2 = 2;

    match (_p1, _p2) {
        (1, 1) => println!("One"),
        (1, 2) => println!("Letssss bora"),
        _ => println!("catch"),
    }
}

enum HockeyPosition {
    Center,
    Wing,
    Defense,
    Goalie,
}

fn next_player (position: HockeyPosition) {
    // passing
}
//could hold multiple tuple of data
enum Clock {
    Sundial(u8),
    Digital(u8, u8),
    Analog(u8, u8, u8),
}

fn tell_time(clock: Clock) {
    match clock {
        Clock::Sundial(hours) => println!("It is about {} o´clock", hours),
        Clock::Analog(hours, minutes, seconds) => println!("It is {} minutes and {} seconds past {} o´clock", minutes, seconds, hours),
        Clock::Digital(hours, minutes) => println!("It is {} minutes past  {}", minutes, hours),
    }
}

struct HockeyPlayer {
    name: String,
    number: u8,
    position: HockeyPosition,
    goals_ytd: u8,
}

fn make_hockey_player () -> HockeyPlayer {
    let player = HockeyPlayer {
        name: String::from("Bryan Rust"),
        number: 14,
        position: HockeyPosition::Wing,
        goals_ytd: 7,
    };

    return player;
}

struct Triangle(u32, u32, u32);

fn is_equilateral(triangle: Triangle) -> bool {
    triangle.0 == triangle.1 && triangle.1 == triangle.2
}

impl HockeyPlayer {
    fn new(name: String, number: u8, position: HockeyPosition) -> HockeyPlayer {
        HockeyPlayer {
            name: name,
            number: number,
            position: position,
            goals_ytd: 0,
        }
    }
    //using &self is to method that only read the values
    fn shoot_puck(&self, seconds_remaning: u16) {
        if seconds_remaning < 300 {
            match self.position {
                HockeyPosition::Center => println!("Gooal"),
                _ => {}
            }
        } else {
            println!("Goal");
        }
    }

    fn shoot_puck_mut(&mut self, seconds_remaning: u16) {
        if seconds_remaning < 300 {
            match self.position {
                HockeyPosition::Center => {
                    self.goals_ytd += 1;
                    println!("Gooal")
                },
                _ => {}
            }
        } else {
            self.goals_ytd += 1;
            println!("Goal");
        }
    }
}


fn structs_enum() {
    // Enum
    tell_time(Clock::Analog(9, 25, 45));

    // Struct

    let player = make_hockey_player();
    println!("{}", player.name);
    let _t = Triangle(3, 4, 5);
    is_equilateral(_t);

    // enum
    enum _Clock {
        Sundial { hours: u8 },
        Digital { hours: u8, minutes: u8 },
        Analog  { hours: u8, minutes: u8, seconds: u8 },
    }

    let _c = _Clock::Analog {
        hours: 9,
        minutes: 24,
        seconds: 3,
    };
    //methods to behaivors
    let mut player2 = HockeyPlayer::new(String::from("Xico"), 18, HockeyPosition::Center);
    //method to read
    // method to write
    //
    player2.shoot_puck(1000);
    player2.shoot_puck(12233);
    player2.shoot_puck_mut(12233);
}

fn main() {
    _main();
    square(2);
    _flow();
    structs_enum();


}
