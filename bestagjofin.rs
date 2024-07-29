// read n then read n lines. Each line is in format s string, x integer. Print s corresponding to the largest x.
use std::io;

fn main() {
    // Read the first line to get the number of entries (n)
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: usize = input.trim().parse().expect("Please enter a valid number");

    // Variables to track the string with the largest integer
    let mut max_string = String::new();
    let mut max_value = i32::MIN;

    // Read n lines in the format "s: string, x: integer"
    for _ in 0..n {
        input.clear();
        io::stdin().read_line(&mut input).expect("Failed to read line");

        // Split the line into string and integer parts
        let parts: Vec<&str> = input.trim().split(' ').collect();
        if parts.len() != 2 {
            eprintln!("Invalid input format, expected 's: string, x: integer'");
            return;
        }

        let s_part = parts[0].trim();
        let x_part = parts[1].trim();

        // Extract the string s
        let s = s_part.strip_prefix("").expect("Expected 's:' prefix").trim();

        // Extract and parse the integer x
        let x: i32 = x_part.strip_prefix("").expect("Expected 'x:' prefix").trim().parse().expect("Invalid integer");

        // Update the maximum value and corresponding string if necessary
        if x > max_value {
            max_value = x;
            max_string = s.to_string();
        }
    }

    // Print the string corresponding to the largest integer
    println!("{}", max_string);
}

