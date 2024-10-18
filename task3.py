def printf(a, b):
    if b != a:
        printf(a, b - 1)
    print(b)
a, b = map(int, input("Введите числа: ").split())
if a < b:
    printf(a, b)
else:
    printf(b, a)
