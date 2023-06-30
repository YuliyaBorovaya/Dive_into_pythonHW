#Напишите программу, которая принимает две строки
#вида “a/b” — дробь с числителем и знаменателем.
#Программа должна возвращать сумму
#и *произведение дробей. Для проверки своего
#кода используйте модуль fractions
from fractions import Fraction
def calc_fractions(fraction1, fraction2):
    num1, denom1 = map(int, fraction1.split('/'))
    num2, denom2 = map(int, fraction2.split('/'))

    fraction_sum = Fraction(num1, denom1) + Fraction(num2, denom2)
    fraction_prod = Fraction(num1, denom1) * Fraction(num2, denom2)

    return fraction_sum, fraction_prod


def calc_fraction(fraction1, fraction2):
    num1, denom1 = map(int, fraction1.split('/'))
    num2, denom2 = map(int, fraction2.split('/'))

    # Вычисляем общий знаменатель
    com_denominator = denom1 * denom2

    # Вычисляем сумму дробей
    numerator_sum = num1 * denom2 + num2 * denom1
    fraction_sum = f"{numerator_sum}/{com_denominator}"

    # Вычисляем произведение дробей
    numerator_prod = num1 * num2
    fraction_prod = f"{numerator_prod}/{denom1 * denom2}"

    return fraction_sum, fraction_prod


fraction1 = input("Введите первую дробь (в виде 'a/b'): ")
fraction2 = input("Введите вторую дробь (в виде 'a/b'): ")

sum_result, product_result = calc_fraction(fraction1, fraction2)
print("Сумма дробей: ", sum_result)
print("Произведение дробей: ", product_result, end='\n')

print("Проверка действий:")
sum_result, product_result = calc_fractions(fraction1, fraction2)
print("Сумма дробей: ", sum_result)
print("Произведение дробей: ", product_result)