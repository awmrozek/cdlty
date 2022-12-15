program lastfactorialdigit;
var n, i, t : integer;
begin
  read(n);
  for i := 1 to n do
    begin
      read(t);
      if t = 1 then
        begin
          writeln(1);
        end

      else if t = 2 then
        begin
          writeln(2);
        end

      else if t = 3 then
        begin
          writeln(6);
        end

      else if t = 4 then
        begin
          writeln(6);
        end

      else
        begin
          writeln('0');
        end;

    end;
end.
