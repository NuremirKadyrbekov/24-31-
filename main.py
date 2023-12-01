print("Трёх значное число")
number = int(input())
if 100 <= number <= 999:
    a = number // 100  
    b = (number // 10) % 10 
    c = number % 10

    if a == c:
        print("палиндромом.")
    else:
        print("Не палиндромом.")
else:
    print("Вы ввели не правильное число! ")