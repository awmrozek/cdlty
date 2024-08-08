// Calculate mean value of n numbers
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    // Read the first line to get the value of n
    let n: usize = lines.next().unwrap().unwrap().trim().parse().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");

    // Read the second line to get the n integers
    let numbers_line = lines.next().unwrap().unwrap();
    let numbers: Vec<i32> = numbers_line.split_whitespace()
                                        .map(|num| num.trim().parse().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly"))
                                        .collect();

    let sum: i32 = numbers.iter().sum();
    let mean = sum as f64 / n as f64;

    // Print the mean value
    println!("{:}", mean as i32);
}
