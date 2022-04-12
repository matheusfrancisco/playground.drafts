fn _immutable () {
    let mut list = vec![1, 2, 3];

    //if remove the  {} it won't work
    //
    {
        let list_first = list.first();
        let list_last = list.last();

        println!(
            "The first element is {:?} and the last is {:?}",
            list_first,
            list_last
        );
    }


    *list.first_mut().expect("list was empty") += 1;
}

pub struct Player {
    score: i32,
}

impl Player {
    pub fn set_score(&mut self, new_score: i32) {
        self.score = new_score;
    }

    pub fn score(&self) -> i32 {
        self.score
    }

    pub fn new() -> Self {
        Player { score: 0 }
    }
}

fn _make_player_score() {
    let mut player1 = Player::new();
    let old_score = player1.score();
    player1.set_score(old_score + 1);
}

fn main() {

}
