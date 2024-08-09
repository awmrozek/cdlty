// read n and m, then read list of strings, concatenate the list, replace character "." with ""
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    // Read the first line to get the values of n and m
    let first_line = lines.next().unwrap().unwrap();
    let mut parts = first_line.split_whitespace();
    let n: usize = parts.next().unwrap().parse().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");
    let _m: usize = parts.next().unwrap().parse().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");

    // Read the next n lines to get the list of strings
    let mut concatenated_string = String::new();
    for _ in 0..n {
        let line = lines.next().unwrap().unwrap();
        concatenated_string.push_str(&line);
    }

    // Replace all occurrences of '.' with an empty string
    let result_string = concatenated_string.replace(".", "");

    // Print the resulting string
    println!("{}", result_string);
}

