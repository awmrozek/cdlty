// Round number to closest decimal
use std::io::{self, Write};

fn main() {
    // Function to read two integers from a single line
    fn read_two_integers(prompt: &str) -> (String, i32) {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");
        let mut iter = input.trim().split_whitespace();
        let n: String = iter.next().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly").to_string();
        let m: i32 = iter.next().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly").parse().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");
        (n, m)
    }

    // Function to read an integer from the user
    fn read_integer(prompt: &str) -> f32 {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");
        input.trim().parse().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly")
    }
    let t = read_integer("");

    
    let ti = t as i32;
    if (t % 1.0) > 0.5 {
        println!("{}", ti + 1);
    } else {
        println!("{}", ti);
    }
}

