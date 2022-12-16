program parking;
var i, j, t, n, x, xmin, xmax : cardinal;

begin

  read(t);

  for i := 1 to t do
    begin

      read(n);
      xmin := 999999;
      xmax := 0;
      for j := 1 to n do
        begin
          read(x);

          if x < xmin then
            begin
              xmin := x;
            end;

          if x > xmax then
            begin
              xmax := x;
            end;
          { write('xmax ');
          write(xmax);
          write('xmin ');
          write(xmin);
          writeln(''); }
        end;
      writeln((xmax - xmin)*2);
    end;
end.

