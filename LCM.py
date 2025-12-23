# LCM = (a*b)/GCD(a,b)

a,b = 28,88

mul = a*b

A,B = max(a,b),min(a,b)

while(B!=0):
    rem = A%B
    A = B
    B = rem


lcm = mul//A

print(lcm)