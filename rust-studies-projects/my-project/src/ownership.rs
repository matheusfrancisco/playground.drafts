// Borrowing

struct Person {
    name: String,
    //middle_name: String,
    //last_name: String,
    //title: String,
    //suffix: String,
    //phone_number: String,
    //address: String,
    //email: String,
    //zodiac: String,
    //blood_type: String,
}

fn congratulate(person: &Person) {
    println!("Congratulation, {}!!!", person.name)
}

fn main() {
    // Ownership
    let s = String::from("book");
    //let plural = __pluralize(s.clone());
    let plural = pluralize(&s);

    println!("I have one {}, you have two {}", s, plural);

    let p = Person {
        name: String::from("Jake"),
    };

    congratulate(&p);
    println!("Can still use p here {}", p.name);

    let v = vec![10, 20, 30];
    let a = [10, 20, 30];
    let v_slice = &v[..];

    only_reference_to_array(&a);
    only_reference_to_vector(&v);
    reference_to_either_array_or_vector(&a[..]);
    reference_to_either_array_or_vector(&v[..]);
    reference_to_either_array_or_vector(&v_slice[0..1]);

}
fn only_reference_to_array(param: &[i32; 3]) {
    println!("array {:?}", param);
}

fn only_reference_to_vector(param: &Vec<i32>) {
    println!("vector {:?}", param);
}

fn reference_to_either_array_or_vector(param: &[i32]) {
    println!("this is a slice {:?}", param);
}
// not good one
fn _pluralize(mut pl: String) -> String {
    pl.push_str("s");
    pl
}

fn __pluralize(singular: String) -> String {
    singular + "s"
}

fn pluralize(singular: &str) -> String {
    singular.to_owned() + "s"
}
