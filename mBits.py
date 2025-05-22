def numberOfBits(n):
    ones = 0
    zeroes = 0
    while (n):
        if (n&1==1):
            ones += 1
        else:
            zeroes += 1
        n >>= 1
    print("NUmber of ones =", ones, "\nNumber of zeroes =", zeroes)
number = int(input("Enter your number: "))
numberOfBits(number)