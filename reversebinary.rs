// Reverse binary - read number, convert to binary, reverse vector, print as decimal
use std::io;

fn main() {
  // Read input from user
  let mut input = String::new();

  io::stdin()
    .read_line(&mut input)
    .expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");

  // Convert input to integer
  let number: u32 = input.trim().parse().expect("This condition should never happen in a Kattis contest. Nonetheless the Rust compiler requires us to handle it properly");

  // Convert the number to binary and store in a vector
  let binary_representation: Vec<u32> = to_binary_array(number);

  // Print the binary array
//  println!("Binary representation: {:?}", binary_representation);
  println!("{}", to_number(binary_representation));
}

fn to_number(mut v: Vec<u32>) -> u32 {
  let mut sum: u32;
  sum = 0;
  let base: u32 = 2;

  for i in 0..v.len() {
    sum += v[i] * (1 << v.len() - i - 1);
//    println!("{}", v[i]);
  }
  sum
}

// Function to convert number to binary array
fn to_binary_array(mut num: u32) -> Vec<u32> {
  let mut binary = Vec::new();

  while num > 0 {
    binary.push(num % 2);
    num /= 2;
  }

  // Reverse the binary vector because we calculate the binary from least significant bit
  //binary.reverse();

  // Handle the case for zero
  if binary.is_empty() {
    binary.push(0);
  }

  binary
}

