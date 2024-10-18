def printf(n):
    if n != 1:
        printf(n - 1)
    print(n)
n = int(input("Введите число: "))
printf(n)
