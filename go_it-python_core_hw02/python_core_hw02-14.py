pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print('Divide by zero completed!')
