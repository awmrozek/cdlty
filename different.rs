// Print absolute value of difference
// Keep reading stdin until EOF
use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main () -> io::Result<()> {
    // ************** read input ******************* //

    // buffer to read data to
    let mut user_input = String::new();

    // To read single line
    //    std::io::stdin().read_line (&mut val).expect("Failed to read line");

    // To read stdin to string
    //    let mut stdin = io::stdin();
    //    stdin.read_to_string(&mut user_input);

    // *************** program logic *************** //


    // todo: does not update val1 val2

    while std::io::stdin().read_line (&mut user_input).expect("Failed to read line") != 0 {
        let mut substr_iter = user_input.split_whitespace();
        let mut next_num = || -> usize {
            substr_iter.next().expect("Not enough input numbers")
                .parse().expect("Input is not a number")
        };

        let val1 = next_num();
        let val2 = next_num();

        if val2 > val1 {
            println!("{}", val2-val1);
        } else {
            println!("{}", val1-val2);
        }
    }

    Ok(())
}

