// Dragafra - read two integers, print max(a,b) - min(a,b)
// Print absolute value of difference
use std::io;
fn main() {
    // Read first number
    // println!("Enter the first number:");
    let mut first_number = String::new();
    io::stdin().read_line(&mut first_number)
        .expect("Failed to read line");
    let first_number: i32 = first_number.trim().parse()
        .expect("Please type a number!");

    // Read second number
    // println!("Enter the second number:");
    let mut second_number = String::new();
    io::stdin().read_line(&mut second_number)
        .expect("Failed to read line");
    let second_number: i32 = second_number.trim().parse()
        .expect("Please type a number!");

    // Determine the difference
    let difference = if first_number > second_number {
        first_number - second_number
    } else {
        second_number - first_number
    };

    // Print the result
    println!("{}", difference);
}
