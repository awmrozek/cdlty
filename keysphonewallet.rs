// Read strings and detect if any of strings "keys" "phone" "wallet" are misssing from the input set
use std::io::{self, Write};

fn main() {
    // Prompt user for the number of strings
    // print!("Enter the number of strings: ");
    io::stdout().flush().unwrap();

    // Read the number of strings (n)
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: usize = input.trim().parse().expect("Please enter a valid number");

    // Create a vector to store the strings
    let mut strings = Vec::new();

    // Read n strings
    for _ in 0..n {
        // print!("Enter a string: ");
        io::stdout().flush().unwrap();
        input.clear();
        io::stdin().read_line(&mut input).expect("Failed to read line");
        let trimmed = input.trim().to_string();
        strings.push(trimmed);
    }

    // Print the collected strings
    let mut keys = false;
    let mut phone = false;
    let mut wallet = false;
    for s in &strings {
    	if (s == "keys") {
	    keys = true;
        }
	if (s == "phone") {
	    phone = true;
        }
        if (s == "wallet") {
            wallet = true;
        }
    }

    if (keys && phone && wallet) {
        println!("ready")
    } else {
        if (!keys) {
            println!("keys")
        }
        if (!phone) {
            println!("phone")
        }
        if (!wallet) {
            println!("wallet")
        }
    }
}

