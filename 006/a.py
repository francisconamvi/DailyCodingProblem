import math

def isPrime(n):
    for x in range(2,math.ceil(math.sqrt(n))):
        if n % x == 0:
            return False
    return True

n = 540924990328592
for x in range(2,n//2+1):
    if(isPrime(x)):
        if(isPrime(n-x)):
            print(f"{x} + {n-x} = {n}")
            quit()
