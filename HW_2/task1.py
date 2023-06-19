#✔ Напишите программу, которая получает целое
#число и возвращает его шестнадцатеричное
#строковое представление. Функцию hex
#используйте для проверки своего результата.


NUMBER = 255
SYSTEM = 16

def convert(number: int, system: int) -> str:
    temp = ''
    while number > 0:
        res = number % system
        if res == 10:
            res = 'a'
        if res == 11:
            res = 'b'
        if res == 12:
            res = 'c'
        if res == 13:
            res = 'd'
        if res == 14:
            res = 'e'
        if res == 15:
            res = 'f'
        temp = temp + str(res)
        number = number // system
    return temp[::-1] #разворот: первое двоеточие где начать, второе двоеточие где закончить

print(convert(NUMBER, SYSTEM))
print(f'Число {NUMBER} в шестнадцатеричной системе {hex(NUMBER)}')





