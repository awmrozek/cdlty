// Print acronym of a word
use std::io::{self, Write};

fn main() {
    let mut input = String::new();

    // Read the input sentence from the user

    // Read numbers in first line
    io::stdin().read_line(&mut input).expect("Failed to read line");

    // Read the actual acronym
    io::stdin().read_line(&mut input).expect("Failed to read line");

    // Trim any trailing newline characters
    let input = input.trim();

    // Split the input into words and collect the first letter of each word
    let first_letters: Vec<char> = input
        .split_whitespace()
        .filter_map(|word| word.chars().next())
        .collect();

    // Print the first letters
    println!("{}", first_letters[1..].iter().collect::<String>());
}

