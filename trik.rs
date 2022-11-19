use std::io::{self, BufRead};

fn main() -> io::Result<()> {
  let mut user_input = String::new();
  let stdin = io::stdin();
  stdin.read_line(&mut user_input);

  let mut el1 = 1;
  let mut el2 = 0;
  let mut el3 = 0;

  for i in user_input.chars() {
    //println!("{}", i);

    let mut t = 0;
    if i == 'A' {
      t = el1;
      el1 = el2;
      el2 = t;
    }

    if i == 'B' {
      t = el3;
      el3 = el2;
      el2 = t;
    }

    if i == 'C' {
      t = el1;
      el1 = el3;
      el3 = t;
    }
  }

  if el1 == 1 {
    println!("1");
  }

  if el2 == 1 {
    println!("2");
  }

  if el3 == 1 {
    println!("3");
  }

  Ok(())
}

