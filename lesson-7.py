

a = int(input())
b = int(input())
c = 0
if b>a:
    for i in range(a, b + 1):
        c += i
    b= b - a + 1
    c=c/b
    print(c)
else :
    print("Введите значение по типу b>a")



