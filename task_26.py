# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 
number=int(input("Enter number: "))
digit=int(input("Enter digit: "))

def get_digit_of_number(numb, dig):
    '''функция принимает на вход два цисла, numb - основание степени, 
    dig - показатель степени и возвращает результат numb в степени dig'''
    if dig==1: return numb
    return numb*(get_digit_of_number(numb, dig-1))

print(get_digit_of_number(number, digit))