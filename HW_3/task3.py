# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

equipment = {'спички': 1, 'стакан': 2, 'накидка': 10, 'комплекс питания': 5, 'фонарик': 3}

def backpack_capacity(capacity: int, equipment: dict) -> list[str]:
    packaging_option = []
    summary = []
    for key, value in equipment.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option


print(backpack_capacity(15, equipment))