import sys


def isPrime(num):
    # assuming number as prime until it's determined as not
    prime = True
    # return false if input is <= 1
    if num <= 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            prime = False
            break
    return prime


def nthPrime(n):
    if n <= 0:
        return "invalid input, number must be greater than or equal to 1"
    # using a counter to track the nth number of prime
    counter = 1
    # initializing 2 as the first prime number
    num = 2
    while counter != n:
        num += 1
        if isPrime(num):
            counter +=1
    print(num)       

def main(argv):
    nthPrime(argv)

if __name__ == "__main__":
    nth_number = int(sys.argv[1])
    main(nth_number)
