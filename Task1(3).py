#taking inputs
import math
print("enter the number:")
n = int(input())
def factorial(n):
 if n==1:
        return 1
 else:
        return n* factorial(n-1)
print("Factrorial of the number is:", factorial(n))

