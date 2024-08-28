// Calculate function y = 1000 + 100 * (x-2020), don't know why it is accepted the second time
use std::io::{self, Write};

fn main() {
    // Prompt the user to enter an integer x
    io::stdout().flush().unwrap();

    // Read the input integer x
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let x: i32 = input.trim().parse().expect("Please enter a valid integer");

    // Calculate y = 2020 + 100 * x
    let y = 1000 + 100 * (x-2020);

    // Print the result
    println!("{}", y);
}
