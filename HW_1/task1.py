# 1..Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других.Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input())
b = int(input())
c = int(input())

if a > b + c or b > a + c or c > a + b:
    print('Треугольника не существует!')
elif a == b == c:
    print('Треугольник существует и является pавносторонним')
elif (a == b and a != c) or (a == c and a != b) or (a != b and b == c):
    print('Треугольник существует и является равнобедренным')
elif a != b != c and a != c:
    print('Треугольник существует и является разносторонний')
