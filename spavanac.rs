// Spavanac - Get time from STDIN and print the t-45 minutes
// Adam Mrozek
// Second Program in Rust
// UwU

use std::io::{self, BufRead};

fn main() -> io::Result<()> {
  let stdin = io::stdin();

  // This is an example of how one can read from STDIN in Rust
  for line in stdin.lock().lines().map(|l| l.unwrap()) {
    let nums: Vec<i64> = line.split_whitespace()
      .map(|num| num.parse().unwrap())
      .collect();

    //for i in nums {
    //  println!("{}", i);
    //}

    let a = nums[0];
    let b = nums[1];

    let mut my_time = a * 60 + b - 45;
    if my_time < 0 {
      my_time = my_time + 24*60;
    }

    let my_hours = my_time / 60;
    let my_minutes = my_time - my_hours*60;

    println!("{} {}", my_hours, my_minutes);
  }

  Ok(())
}

