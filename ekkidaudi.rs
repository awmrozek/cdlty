// ekkidaudi - ekki opna daudi inni
use std::io;

fn main() {
    // Create a new String to store user input
    let mut input1 = String::new();
    let mut input2 = String::new();

    // Read the first string
    //println!("Enter the first string (use '|' to separate values):");
    io::stdin().read_line(&mut input1).expect("Failed to read input");
    
    // Read the second string
    //println!("Enter the second string (use '|' to separate values):");
    io::stdin().read_line(&mut input2).expect("Failed to read input");

    // Trim the input to remove any trailing newlines
    let input1 = input1.trim();
    let input2 = input2.trim();

    // Split the strings by the '|' character and collect them into vectors
    let parts1: Vec<&str> = input1.split('|').collect();
    let parts2: Vec<&str> = input2.split('|').collect();

    // Print the results for the first string
    println!("{}{} {}{}", parts1[0], parts2[0], parts1[1], parts2[1]);
}

