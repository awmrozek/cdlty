// Compare strings and set boolean flag true/false depending on input string
use std::io::{self, BufRead};

fn main() {
    // Create a mutable String to store the input
    let mut input = String::new();

    // Read the first line from standard input (which should be the integer n)
    io::stdin().read_line(&mut input).expect("Failed to read line");

    // Parse the input to get the integer n
    let n: usize = input.trim().parse().expect("Please enter a valid number");

    // Create a vector to store the lines
    let mut lines = Vec::new();

    // Read n lines from standard input
    for _ in 0..n {
        let mut line = String::new();
        io::stdin().read_line(&mut line).expect("Failed to read line");
        lines.push(line.trim().to_string());
    }

    // Print each line without quotes
    let mut nautakjot = false;
    let mut kjuk = false;
    for line in lines {
    	if (line == "nautakjot") {
		nautakjot = true;
	}
	if (line == "kjuklingur") {
		kjuk = true;
	}
        // println!("Takk {}", line);
    }
    if (nautakjot && kjuk) {
    	println!("blandad best");
    } else if (nautakjot) {
    	println!("nautakjot");
    } else {
    	println!("kjuklingur");
    }
}
