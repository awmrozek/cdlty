use std::io;
use std::io::Read;

fn main() {
    let mut input =  Vec::new();
    let stdin = std::io::stdin();
    let mut handle = stdin.lock();
    handle.read_to_end(&mut input);
    print!("{}", input[0]-48)
}
