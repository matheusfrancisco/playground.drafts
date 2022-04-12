use std::collections::HashMap;

fn counting_freq() {
    let text = "hello world hello";
    let mut freqs = HashMap::new();

    /* signature of the entry method
     pub fn entry(&mut self, key: K) -> Entry<K, V>
     Entry num has Occupied or Vacant
     pub fn or_insert(self, default: V) -> &'a mut V
    */

    for word in text.split_whitespace() {

        *freqs.entry(word).or_insert(0) += 1;

       /* match freqs.get_mut(word) {
            Some(value) => *value += 1;
            None => {
                freqs.insert(word, 1);
            }
        }*/
    }

    println!("Word frequencies: {:#?}", freqs);
}

#[derive(Debug)]
pub structs Stats {
    hp: u8,
    sp: u8,
}

#[derive(Debug)]
pub struct Monster {
    stats: Stats,
    friends: Vec<Friend>,
}

#[derive(Debug)]
pub struct Friend {
    loyalty: u8,
}

impl Monster  {
    pub fn final_breath(&mut self) {
        if let Some(friend) = self.friends.first() {
            self.stats.heal(friend.loyalty);
            println!("Healing for {}", friend.loyalty);
        }
    }
}

impl Stats {
    pub fn heal(&mut self, amount: u8) {
         self.hp += friend.loyalty;
         self.sp -= friend.loyalty;
    }
}

fn main() {


}
