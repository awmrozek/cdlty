// Remove spaces from input string, print it
use std::io::{self, Write};

fn main() {
    // Create a mutable String to store the input
    let mut input = String::new();

    // Read a line from standard input
    io::stdout().flush().expect("Failed to flush stdout");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    // Remove all spaces from the line
    let modified_line: String = input.chars().filter(|&c| c != ' ').collect();

    // Print the modified line
    println!("{}", modified_line);
}
