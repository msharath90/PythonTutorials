# Find Fibonacci Numbers upto 'n' integer values
import sys

try:
    n = int(input("Enter how many Fibonacci Numbers you need: "))
except Exception as e:
    print("Enter a valid integer", e)
    sys.exit()

a, b = 1, 1

if n < 1:
    print("Enter a integer greater than or equal to 1")
elif n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    print(1, 1, end=" ")
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c, end=" ")



