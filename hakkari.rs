// Hakkari - count stars in standard input
use std::io;

fn main() {
    let mut input = String::new();
    
    // Read the dimensions n and m
    io::stdin().read_line(&mut input).expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");
    let dims: Vec<usize> = input
        .trim()
        .split_whitespace()
        .map(|s| s.parse().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly"))
        .collect();
    let (n, m) = (dims[0], dims[1]);
    
    let mut grid = Vec::new();
    
    // Read the grid of characters
    for _ in 0..n {
        input.clear();
        io::stdin().read_line(&mut input).expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");
        grid.push(input.trim().chars().collect::<Vec<_>>());
    }

    // Count indices of '*' characters
    let mut count = 0;
    for i in 0..n {
        for j in 0..m {
            if grid[i][j] == '*' {
              count += 1;
            }
        }
    }
   
    // Print indices of '*' characters
    println!("{}", count);
    for i in 0..n {
        for j in 0..m {
            if grid[i][j] == '*' {
                println!("{} {}", i+1, j+1);
            }
        }
    }
}
