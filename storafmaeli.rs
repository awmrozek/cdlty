// Check if a number is evenly divisible by 10
use std::io;

fn main() {
    // Read a number from input
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("Failed to read line");

    // Parse the input to an integer
    let number: i32 = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Please enter a valid number.");
            return;
        }
    };

    // Check if the number is evenly divisible by 10
    if number % 10 == 0 {
        println!("Jebb");
    } else {
        println!("Neibb");
    }
}
