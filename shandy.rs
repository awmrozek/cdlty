// Print min(a, b)*2
use std::io;
use std::io::Read;

fn main() {
	let mut s = String::new();
	std::io::stdin().read_to_end(&mut s).expect("read_line error");

	let mut parts = s.split_whitespace().map(|s| s.parse::<i32>());
	//match (parts.next(), parts.next()) {
	//    (Some(Ok(a)), Some(Ok(b))) => {
		// a and b are i32
	//    }
	    // handle other problems: not enough numbers, numbers are invalid, etc
	//    _ => {}  // ignore invalid input
	//}

	let a = parts.next().unwrap().unwrap();
	let b = parts.next().unwrap().unwrap();

	print!("{}", min(a, b)*2)
}

