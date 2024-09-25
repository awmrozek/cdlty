// Print first character of input line
use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("Failed to read line");

    let trimmed_input = input.trim();

    if let Some(first_char) = trimmed_input.chars().next() {
        println!("{}", first_char);
    } else {
        println!("");
    }
}
