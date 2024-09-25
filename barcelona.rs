use std::io;

fn main() {
	// Create a mutable String to store the input
	let mut input = String::new();

	// Read the first line from standard input (which should contain n and m)
	io::stdin().read_line(&mut input).expect("Failed to read line");

	// Parse the input to get n and m
	let mut iter = input.trim().split_whitespace();
	let n: usize = iter.next().expect("Missing n").parse().expect("Please enter a valid number for n");
	let m: i32 = iter.next().expect("Missing m").parse().expect("Please enter a valid number for m");

	// println!("n: {}, m: {}", n, m); // Optional: Print n and m to verify
	let mut a_str = String::new();
	io::stdin().read_line(&mut a_str).expect("read error");
	let mut numbers = a_str.split_whitespace()
	    .map(|x| x.parse::<i32>().expect("parse error"))
	        .collect::<Vec<i32>>();

	for i in 0..n {
		if (numbers[i] == m) {
			if (i == 0) {
				let res = "fyrst";
				println!("{}", res);
			}
			else if (i == 1) {
				let res = "naestfyrst";
				println!("{}", res);
			} else {
				let res = format!("{}{}", i+1, " fyrst");
				println!("{}", res);
			}
		}
	}
	// Print the numbers to verify
	//println!("{:?}", numbers);
}

