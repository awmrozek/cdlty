// For two coordinates in Cartesian system, determine which
// quadrant they belong to (1,2,3,4)
// Adam Mrozek 2022
// First program in Rust
use std::io;

fn main() -> io::Result<()> {
  let mut user_input = String::new();
  let mut user_input2 = String::new();
  let stdin = io::stdin();

  stdin.read_line(&mut user_input);
  stdin.read_line(&mut user_input2);

  //let mut x: i32 = user_input.parse().unwrap();
  //let mut y: i32 = user_input2.parse().unwrap();
                                            // Is this really necessary?
  let mut x: i32 = user_input.trim().parse().expect("");
  let mut y: i32 = user_input2.trim().parse().expect("");

  if (x > 0 && y > 0) {
    println!("1");
  }
  
  if (x < 0 && y > 0) {
    println!("2");
  }

  if (x < 0 && y < 0) {
    println!("3");
  }

  if (x > 0 && y < 0) {
    println!("4");
  }

  Ok(())
}

