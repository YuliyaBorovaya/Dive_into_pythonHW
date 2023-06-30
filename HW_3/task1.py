# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


# список для обработки
my_list_1 = [1, 1, 2, 3, "A", "T", "A", 3, "o", "0", 0]
my_list_2 = [1, 2, 3, 4, "A", "J", "X", "X", "0", 0, 8]


# обработка списка
def double_items(work_list: list) -> list:
    return list(set([i for i in work_list if work_list.count(i) > 1]))


def main():
    print(f"{my_list_1} - {double_items(my_list_1)}")
    print(f"{my_list_2} - {double_items(my_list_2)}")


if __name__ == "__main__":
    main()