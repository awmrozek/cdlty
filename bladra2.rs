// Calculate S = v0t + 1/2 at^2
use std::io;

fn main() {
	let mut input = String::new();
	io::stdin().read_line(&mut input)
		.expect("Failed to read line");

	// Split the input by whitespace and collect into a vector
	let numbers: Vec<i32> = input
		.trim() // Remove any trailing whitespace/newline
		.split_whitespace() // Split the input by whitespace
		.map(|s| s.parse().expect("Please enter a number")) // Parse each part as an i32
		.collect(); // Collect the parsed numbers into a vector


	let v: f64 = numbers[0].into();
	let a: f64 = numbers[1].into();
	let t: f64 = numbers[2].into();

	println!("{}", v*t + 0.5*a*t*t)
}
