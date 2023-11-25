-- funkcja :: Num a => [a] -> [a]
funkcja [] = [1]
funkcja (x:xs) = if (x /= 0) then (x:funkcja xs) else (1:funkcja xs)
condition x = x /= 0

funkcja3 :: [Integer] -> Integer
funkcja3 [] = 1
funkcja3 (x:xs) = x * funkcja3 xs
funkcja2 = (filter (\x -> x /= 0))

funkcja0 :: [Integer] -> Integer
funkcja0 = funkcja3 . funkcja2
-- funkcja (x:xs) = x:(funkcja xs)
-- stdin?
main = putStrLn "VELKOMIN!"
