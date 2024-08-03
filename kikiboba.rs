// Count number of k's and b's in a string
use std::io::{self, Write};

fn main() {
    io::stdout().flush().unwrap();

    // Read the input string
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let input = input.trim();

    // Initialize counters for 'k' and 'b'
    let mut k_count = 0;
    let mut b_count = 0;

    // Iterate through each character in the string and count 'k' and 'b'
    // this is nice new way, never heard of match
    for ch in input.chars() {
        match ch {
            'k' => k_count += 1,
            'b' => b_count += 1,
            _ => {}
        }
    }

    // Program logic
    if (k_count == b_count && k_count > 0) {
        println!("boki")
    }

    else if (k_count > b_count) {
        println!("kiki");
    }

    else if (b_count > k_count) {
        println!("boba");
    }

    else if (k_count == 0 && b_count == 0) {
        println!("none");
    }
}

