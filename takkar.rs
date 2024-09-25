// Read two integers, compare
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


        if sum > sum2 {
                println!("MAGA!");
        } else if sum < sum2 {
                println!("FAKE NEWS!");
        } else {
                println!("WORLD WAR 3!");
        }
}

