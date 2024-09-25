// Read string from input, print string and input string
use std::io;

fn main() {
    // Read a line of input
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("Failed to read line");

    // Print "BANANA" followed by the input line
    println!("Kvedja,");
    println!("{}", input.trim());
}

