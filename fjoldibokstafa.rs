// Print length of input string
use std::io::{self, Write};

fn main() {
    // Prompt the user to enter a string
    io::stdout().flush().unwrap();

    // Read the input string
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let input = input.trim();

    // Calculate the length of the string
    let length = input.len();

    // Print the length of the string
    println!("{}", length);
}
