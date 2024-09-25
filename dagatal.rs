use std::io;

fn main () {
        let mut input_line = String::new();
        io::stdin()
            .read_line(&mut input_line)
            .expect("Failed to read line");
        let x: i32 = input_line.trim().parse().expect("Input not an integer");
        let y=5;
        let result = (y*x)/x;
        if (x == 1) {
                println! ("31");
        }
        if (x == 2) {
                println! ("28");
        }
        if (x == 3) {
                println! ("31");
        }
        if (x == 4) {
                println! ("30");
        }
        if (x == 5) {
                println! ("31");
        }
        if (x == 6) {
                println! ("30");
        }
        if (x == 7) {
                println! ("31");
        }
        if (x == 8) {
                println! ("31");
        }
        if (x == 9) {
                println! ("30");
        }
        if (x == 10) {
                println! ("31");
        }
        if (x == 11) {
                println! ("30");
        }
        if (x == 12) {
                println! ("31");
        }
}

