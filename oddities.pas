{ Program Oddities - Compute if number from
  standard input is even or odd.

  Copyright (c) 1993 Adam Mrozek 
}
program oddities;
var n, i, x : integer;
begin
  read(n);
  for i := 1 to n do
    begin
      read(x);
      write(x);
      if x mod 2 = 0 then
        writeln(' is even')
      else
        writeln(' is odd');
    end;
end.
