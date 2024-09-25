use std::io::{self, Write};

fn main() {
    // Function to read an integer from the user
    fn read_integer(prompt: &str) -> i32 {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");
        input.trim().parse().expect("Please enter a valid integer")
    }

    // Read n
    let n = read_integer("Enter the number of integers (n): ");

    // Read m (though m is not used in this calculation, it is read as per the instruction)
    let m = read_integer("Enter another integer (m): ");

    // Initialize the sum
    let mut sum = 0;

    // Read n integers and sum them up
    for _ in 0..n {
        let num = read_integer("Enter an integer: ");
        sum += num;
    }

    // Print the result
    println!("The sum of the {} integers is: {}", n, sum);
    if (sum < m) {
        println!("Nebb")
    } else {
        println!("Jebb")
    }
}

