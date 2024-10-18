def pow(a):
    if a == 2:
        return "YES"
    elif a % 2 != 0:
        return "NO"
    else:
        return pow(a // 2)
a = int(input("Введи число: "))
print(pow(a))
