# kankuklatr yasash
"""
birinchi raqam
ikkinchi raqam
amal =-*/**

amal qoshuv birinchi + ikkinchin
amal ayruv birinchi - ikkinchin
"""

a = int(input("birinchi raqamni kiriting: "))
b = int(input("ikkinchi raqamni kiriting: "))
amal = input("+, -, /, *, //, **\namallardan birini tanlang > 15")

if amal == "+":
    print(f"{a} + {b} = {a + b}")
elif amal == "-":
    print(f"{a} - {b} = {a - b}")
elif amal == "/":
    print(f"{a} / {b} = {a / b}")
elif amal == "*":
    print(f"{a} * {b} = {a * b}")
elif amal == "//":
    print(f"{a} // {b} = {a // b}")
elif amal == "**":
    print(f"{a} ** {b} = {a ** b}")
else:
    print("Bunaqa aml yoq")