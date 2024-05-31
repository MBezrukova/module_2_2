#На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Ввведите третье число: "))
if first == second and second == third:
    print("3")
elif first == second or second == third or first == third:
    print("2")
else:
    print("0")