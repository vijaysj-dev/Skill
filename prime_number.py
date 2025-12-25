import math as m
def prime_or_not(x):
    for i in range(2,int(m.sqrt(x))+1):
        if x%i == 0:
            return False
        
    return True

print(prime_or_not(44))