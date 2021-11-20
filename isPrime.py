def isPrime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True

def isPrimeByFactors(number):
    factors = []
    for i in range(2, number):
        if number % i == 0: # i is a factor
            factors.append(i)
    if len(factors) == 0:
        return True
    else:
        print(factors)
        return False
        


##### Driver ######

def main():
    number = int(input("number to test: "))
    print(str(isPrimeByFactors(number)))

main()
