// Sum list of integers in Rust without typo
use std::io::{self, Write};

fn main() {
    // Function to read two integers from a single line
    fn read_two_integers(prompt: &str) -> (i32, i32) {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");
        let mut iter = input.trim().split_whitespace();
        let n: i32 = iter.next().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly").parse().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");
        let m: i32 = iter.next().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly").parse().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");
        (n, m)
    }

    // Function to read an integer from the user
    fn read_integer(prompt: &str) -> i32 {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");
        input.trim().parse().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly")
    }

    // Read n and m
    let (n, m) = read_two_integers("");

    // Initialize the sum
    let mut sum = 0;

    // Read n integers and sum them up
    for _ in 0..n {
        let num = read_integer("");
        sum += num;
    }


    if (m < sum) {
        println!("Neibb");
    } else {
        println!("Jebb");
    }
}

