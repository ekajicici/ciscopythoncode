num = int(input("how many bottles do you want:"))
lit = int(input("enter liter size:"))
print("you got", num, " bottles of", lit, "liters")
if lit <= 1:
    n = num * 0.10
    print("your deposit is =", n)
else:
    nn = num * 0.25
    print("your deposit is =", nn)
