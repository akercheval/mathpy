dist x1 y1 x2 y2 = sqrt (((x2 - x1) ** 2) + ((y2 - y1) ** 2))

pfdriver x1 y1 x2 y2 rad matches 
    | x2 == 11 && y2 == 11 = matches
    | y2 == 11 = pfdriver x1 y1 (x2 + 1) (-10) rad matches
    | x1 == x2 = pfdriver x1 y1 (x2 + 1) y2 rad matches
    | y1 == y2 = pfdriver x1 y1 x2 (y2 + 1) rad matches
    | otherwise = 
        if dist x1 y1 x2 y2 == rad
            then pfdriver x1 y1 x2 (y2 + 1) rad (matches ++ [(x2, y2)])
        else pfdriver x1 y1 x2 (y2 + 1) rad matches

ptsfinder x y rad = pfdriver x y (-10) (-10) rad []
