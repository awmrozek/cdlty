// count number of changed characters between 2 strings
use std::io::{self, Write};

fn main() {
    // Function to read a string from the user
    fn read_string(prompt: &str) -> String {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("This will never happen in a Kattis contest. Nonetheless Rust compiler requires us to handle this case properly.");
        input.trim().to_string()
    }

    // Read the first string
    let string1 = read_string("");

    // Read the second string
    let string2 = read_string("");

    // Iterate through the characters of both strings
    let mut count: i32 = 1;
    for (char1, char2) in string1.chars().zip(string2.chars()) {
        if (char1 != char2) {
            count +=1;
        }
    }
    println!("{}", count);
}

