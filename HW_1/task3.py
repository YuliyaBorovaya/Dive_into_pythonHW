# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 1

print("Компьютер загадал число от 0 до 1000. Отгадайте его. У вас 10 попыток")
while count <= 10:
    a = int(input(str(count) + '-я попытка: '))
    if a > num:
        print('Перебор, попробуйте еще')
    elif a < num:
        print('Недобор, попробуйте еще')
    else:
        print('Вы угадали с %d-й попытки' % count)
        break
    count += 1
else:
    print('Вы исчерпали 10 попыток. Было загадано число', num)



