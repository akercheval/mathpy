import math
def dist(x1, x2, y1, y2):
    radical = ((x1 - x2)**2 + (y1 - y2)**2)
    if radical > 0:
        return math.sqrt(radical)
    else:
        return 0

def pprint(radii):
    for radius in radii:
        print("with radius of " + str(radius) + ":")
        matches = radii[radius]
        for match in matches:
            print(str(match))
    

def generate_good_circle():
    radii = {}
    matches = []

    x = int(input("x coord of center: "))
    y = int(input("y coord of center: "))
    for rad in range(2, 20): # arbitrary range
        for temp_x in range((x - rad), (x + rad + 1)):
            for temp_y in range((y - rad), (y + rad + 1)):
                if dist(x, temp_x, y, temp_y) == rad:
                    if x == temp_x or y == temp_y: # avoid points that are on the same horizontal or vertical line as center
                        break
                    new_match = (temp_x, temp_y)
                    matches.append(new_match)
        if len(matches) != 0:
            radii[rad] = matches
            matches = []
    pprint(radii)

generate_good_circle()
