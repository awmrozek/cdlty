// Read string from first line n from seconds line, print string n times
use std::io;

fn main() {
    // Read the name from the first line
    let mut name = String::new();
    io::stdin().read_line(&mut name).expect("Failed to read line");
    let name = name.trim(); // Remove any trailing newline

    // Read the age from the second line
    let mut age_input = String::new();
    io::stdin().read_line(&mut age_input).expect("Failed to read line");
    let age: usize = age_input.trim().parse().expect("Please enter a valid number");

    // Print the message "Hipp hipp hurra, name!" age times
    for _ in 0..age {
        println!("Hipp hipp hurra, {}!", name);
    }
}
