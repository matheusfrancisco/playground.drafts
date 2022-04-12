
// How to create and use a mutable reference
// in functions,. in first parameter of methods
//
// Borrowing Rules involving mutability
// Example of a porblem prevented by the borrowing rules

#[derive(Debug)]
struct Bucket {
    liters: u32,
}

fn pour(source: &mut Bucket, target: &mut Bucket, amount: u32) {
    source.liters -= amount;
    target.liters += amount;
}

#[derive(Debug)]
struct CarPool {
    passengers: Vec<String>,
}

impl CarPool {
    fn pick_up(&mut self, name: String) {
        self.passengers.push(name);
    }
}

fn main() {
    let mut b1 = Bucket { liters: 20 };
    let mut b2 = Bucket { liters: 10 };
    pour(&mut b1, &mut b2, 1);

    println!("b1 {:?}", b1);
    println!("b2 {:?}", b2);

    let mut car_pool = CarPool {
        passengers: vec![],
    };

    car_pool.pick_up(String::from("Xico"));
    println!("carpool {:?}", car_pool);

    car_pool.pick_up(String::from("May"));
    println!("carpool {:?}", car_pool);

    let list  = vec![1, 2, 3];
    for item in &list {
        println!("item is {}", item);
       // not work list.push(item + 1);

    }
}
