ef factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return factorial(x - 1) * x

x = int(input("Введи число:"))
print(factorial(x))
