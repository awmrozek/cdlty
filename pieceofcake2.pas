program pieceofcake2;
var n, h, v, maxv : cardinal;
var vol : array [1 .. 4] of cardinal;
begin
  read(n);
  read(h);
  read(v);

  vol[1] := h * v;
  vol[2] := h * (n - v);
  vol[3] := (n-h) * v;
  vol[4] := (n-h) * (n - v);

  if (vol[1] > vol[2]) then
    begin
      maxv := vol[1];
    end
  else
    begin
      maxv := vol[2];
    end;

  if vol[3] > maxv then
    begin
      maxv := vol[3];
    end;

  if vol[4] > maxv then
    begin
      maxv := vol[4];
    end;
  // Each cake is 4 cm heigh
  writeln(maxv*4);
end.

