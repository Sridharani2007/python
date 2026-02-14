def add(a, b):
    return a + b

def sub(c, d):
    return c - d

def mul(e, f):
    return e * f

def div(g, h):
    return g / h


print("============================")
print("1. TO PERFORM ADDITION")
print("2. TO PERFORM SUBTRACTION")
print("3. TO PERFORM MULTIPLICATION")
print("4. TO PERFORM DIVISION")
print("5. EXIT")
print("============================")

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter the 1st value: "))
        b = int(input("Enter the 2nd value: "))
        print("Result:", add(a, b))

    elif choice == 2:
        c = int(input("Enter the 1st value: "))
        d = int(input("Enter the 2nd value: "))
        print("Result:", sub(c, d))

    elif choice == 3:
        e = int(input("Enter the 1st value: "))
        f = int(input("Enter the 2nd value: "))
        print("Result:", mul(e, f))

    elif choice == 4:
        g = int(input("Enter the 1st value: "))
        h = int(inpu
