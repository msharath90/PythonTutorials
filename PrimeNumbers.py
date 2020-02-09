# Identify all prime numbers from a given list
from math import sqrt, ceil

lst = [19, 22, 45, 78, 33, 29, 4, 331]
lstNew = {}


def isPrime(elem):
    for i in range(2, ceil(sqrt(elem) + 1)):
        if elem % i == 0:
            return "Not Prime"
    else:
        return "Prime"


for a in lst:
    lstNew.update({a: isPrime(a)})

print(lstNew)
