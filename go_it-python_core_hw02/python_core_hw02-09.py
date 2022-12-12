first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = min(first, second)
while first % gcd or second % gcd:
    gcd -= 1
