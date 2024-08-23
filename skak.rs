// Read 2 lines with numbers, check if line1[0] == line2[0] or line2[1] == line2[1]
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let numbers_line = lines.next().unwrap().unwrap();
    let numbers: Vec<i32> = numbers_line.split_whitespace().map(|num| num.trim().parse().expect("This will never happen nonetheless the Rust compiler requires to handle this in a proper way")).collect();

    let numbers_line_2 = lines.next().unwrap().unwrap();
    let numbers_2: Vec<i32> = numbers_line_2.split_whitespace().map(|num| num.trim().parse().expect("This condition will never happen either. But since we are in Rust we are required to parse this condition properly nontheless")).collect();

    let sum: i32 = numbers.iter().sum();
    let sum2: i32 = numbers_2.iter().sum();

    if (numbers[0] == numbers_2[0] || numbers[1] == numbers_2[1]) {
        println!("1");
    } else {
        println!("2");
    }
}

