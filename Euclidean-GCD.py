a = int(input("Input the first number: "))
b = int(input("Input the second number: "))

if (a <= b): #if a <= b, swap
    t = a
    a = b
    b = t

r = a % b
while ( r > 0):
    a = b
    b = r
    r = a % b

gcd = b

print("The greatest common digit is {0}.".format(gcd))
