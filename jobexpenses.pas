program jobexpenses;
var n, i, tt : integer;
var sum, t : cardinal;
begin
  read(n);
  sum := 0;
  for i := 1 to n do
    begin
      read(tt);
      if (tt < 0) then
        begin
          t := -tt;
          writeln(t);
          sum := sum + t;
        end;
    end;
  writeln(sum);
end.
