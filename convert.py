'''
Реализуйте функцию convert(), которая принимает один аргумент:
    - string — произвольная строка
Функция должна возвращать строку string:
    - полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
    - полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
    - полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает

Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию
convert(), но не код, вызывающий ее.
Примечание 3. Тестовые данные доступны по ссылкам:
'''


def convert(string):
    l = len(list(filter(lambda x: x.islower(), string)))
    u = len(list(filter(lambda x: x.isupper(), string)))
    return string.upper() if u > l else string.lower()



# TEST_1:
print(convert('BEEgeek'))

# TEST_2:
print(convert('pyTHON'))

# TEST_3:
print(convert('pi31415!'))

# TEST_4:
print(convert('ABCDEF'))

# TEST_5:
print(convert('abcdef'))

# TEST_6:
print(convert('12345!?'))

# TEST_7:
print(convert('PI31415!'))

# TEST_8:
print(convert('ABCdef'))

# TEST_9:
print(convert('ABCdef123'))

# TEST_10:
print(convert('AbCdEf12345'))

# TEST_11:
print(convert('dEfAbC'))