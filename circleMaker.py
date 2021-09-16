import math
def dist(x1, x2, y1, y2):
    radical = ((x1 - x2)**2 + (y1 - y2)**2)
    if radical > 0:
#        print(str(math.sqrt(radical)))
        return math.sqrt(radical)
    else:
        return 0
    

def generate_good_circle():
    x = int(input("x coord of center: "))
    y = int(input("y coord of center: "))
#    rad = int(input("radius: "))
    for rad in range(2, 20):
        print("radius: " + str(rad))
        for temp_x in range((x - rad), (x + rad + 1)):
            for temp_y in range((y - rad), (y + rad + 1)):
                if dist(x, temp_x, y, temp_y) == rad:
                    if x == temp_x or y == temp_y:
                        break
                    print("There's one  at (" + str(temp_x) + "," + str(temp_y) + ")")

generate_good_circle()
