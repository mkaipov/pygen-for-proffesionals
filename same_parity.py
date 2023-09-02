"""
Реализуйте функцию same_parity(), которая принимает один аргумент:

    - numbers — список целых чисел

Функция должна возвращать новый список, элементами которого являются числа из
списка numbers, имеющие ту же четность, что и первый элемент этого списка.
"""


def same_parity(numbers: list):
    return list(filter(lambda x: x % 2 == numbers[0] % 2, numbers))


print(same_parity([6, 0, 67, -7, 10, -20]))
print(same_parity([]))
