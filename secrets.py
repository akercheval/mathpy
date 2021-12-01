# Some secret recursive functions: what do they do?
# Written by Adam Kercheval for LCRT quad literacy set, 12/1/21
# For academic use, personal use, whatever: MIT license

# Function 1:
def f_one(n):
    if n == 1:
        return 1
    return n * f_one(n - 1)


# Function 2
def f_two(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return f_two(n - 1) + f_two(n - 2)

# Function 3
def f_three(n, i = 2):
    if n < 2:
        print("Invalid input")
    if n == i:
        return True
    if n % i == 0:
        return False
    return f_three(n, i + 1)
    
#num = int(input("number: "))
#print(f_three(num))
