-- Print Diamond Shape
line :: Int -> Int -> String
line n i = replicate (div (n-1) 2 - i + 1) ' ' ++ replicate (2*i+1) '0'

printDiamond :: Int -> IO ()
printDiamond n = mapM_ (putStrLn . line n) (r ++ (n2 : reverse r))
        where n2 = div n 2
              r = [0 .. n2-1]

