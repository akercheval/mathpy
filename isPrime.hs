factors n = [x | x <- [2..n - 1], n `mod` x == 0]
isPrime n = length (factors n) == 0

myPrime n = foldl (\acc x -> if n `mod` x == 0 then (False, x) else acc) (True, 0) [2..n - 1]
