print("Введите выражение: ")
a, b, c = input().split()
a = int(a)
c = int(c)
if a in range(1,11) and c in range(1,11):
    if b == "+":
        print(a+c)
    elif b =="-":
        print(a-c)
    elif b =="*":
        print(a*c)
    elif b=="/":
        print(a//c)
    else:
        print ("Введите корректный оператор: + - * /")
else:
    print ("Введите значения от 1 до 10")






