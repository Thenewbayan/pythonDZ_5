# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

number_a=int(input("Enter number A: "))
number_b=int(input("Enter number B: "))
def get_summ_recurs(numb_A, numb_B):
     '''Функция принимает два числа и находит их сумму уменьшением/увеличением каждого на 1'''
     if numb_B==0: return numb_A
     return (numb_A+1)+(numb_B-1)

print(f" Сумма чисел {number_a} и {number_b} через рекурсию равна: {get_summ_recurs(number_a, number_b)}")



