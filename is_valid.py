"""
Будем считать, что PIN-код является корректным, если он удовлетворяет следующим условиям:
    - состоит из 4, 5 или 6 символов
    - состоит только из цифр (0−9)
    - не содержит пробелов

Реализуйте функцию is_valid(), которая принимает один аргумент:
    - string — произвольная строка
Функция должна возвращать значение True, если строка string представляет собой
корректный PIN-код, или False в противном случае.
"""


def is_valid(string: str):
    return all(i.isdigit() for i in list(string)) and 6 >= len(string) >= 4


print(is_valid('4367'))
print(is_valid('92134'))
print(is_valid('89abc1'))
print(is_valid('900876'))
print(is_valid('49 83'))
print(is_valid('一一一一一'))
print(is_valid('٠١٢٣٤'))
print(is_valid('🄁🄂🄃🄄🄅'))
