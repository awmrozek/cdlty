// Read integers from stdin until EOF and print them in reverse order
// like unix tac

use std::io::{self, BufRead};

fn main() {
        // Create a vector to store the integers
        let mut numbers = Vec::new();

        // Read integers from standard input until EOF
        let stdin = io::stdin();
        for line in stdin.lock().lines() {
                let line = line.expect("Failed to read line");
                let number: i32 = line.trim().parse().expect("Please enter a valid integer");
                numbers.push(number);
        }

        // Print the numbers in reverse order
        for number in numbers.iter().rev().take(numbers.len()-1) {
                println!("{}", number);
        }
}

