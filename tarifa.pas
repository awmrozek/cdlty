{
Free Pascal Compiler version 3.2.2+dfsg-9ubuntu1 [2022/04/11] for x86_64
Copyright (c) 1993-2021 by Florian Klaempfl and others
}

{ Tarifa.PAS - Compute the amount of megabytes per has after n months.
  Copyright (c) 1983... wait no... it's 2022.

  But Pascal and synthwave are still alive!
}

program tarifa;
var x, n, i, ppi, sum : integer;
begin
  sum := 0;
  read(x);
  read(n);
  
  for i := 1 to n do
  begin
    read(ppi);
    {write('Per used ');
    write(ppi);
    write(' mB this month. ');}

    {write('Per received ');
    write(x);
    write(' credit this month. ');}
    sum := sum + x;
    if sum - ppi >= 0 then
      sum := sum - ppi;
    {write('Per has ');
    write(sum);
    writeln(' mB');}
  end;
  
  writeln(sum+x);
end.
