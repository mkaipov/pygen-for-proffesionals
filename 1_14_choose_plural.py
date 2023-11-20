def choose_plural(amount, declensions):
    if int(str(amount)[-1]) == 1 and int(str(amount)[-2:]) not in [11,12,13,14]:
        return f'{amount} {declensions[0]}'
    elif 2 <= int(str(amount)[-1]) <= 4 and int(str(amount)[-2:]) not in [11,12,13,14]:
        return f'{amount} {declensions[1]}'
    else:
        return f'{amount} {declensions[2]}'


# INPUT DATA:

# TEST_1:

assert choose_plural(21, ('пример', 'примера', 'примеров')) == '21 пример'

# TEST_2:
assert (choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей'))) == '92 гвоздя'

# TEST_3:
assert(choose_plural(8, ('яблоко', 'яблока', 'яблок'))) == '8 яблок'

# TEST_4:
assert(choose_plural(111223, ('копейка', 'копейки', 'копеек'))) == '111223 копейки'

# TEST_5:
assert(choose_plural(763434, ('рубль', 'рубля', 'рублей'))) == '763434 рубля'

# TEST_6:
assert(choose_plural(512312, ('цент', 'цента', 'центов'))) == '512312 центов'

# TEST_7:
assert(choose_plural(59, ('помидор', 'помидора', 'помидоров'))) == '59 помидоров'

# TEST_8:
assert(choose_plural(23424157, ('огурец', 'огурца', 'огурцов'))) == '23424157 огурцов'

# TEST_9:
assert(choose_plural(240, ('курица', 'курицы', 'куриц'))) == '240 куриц'

# TEST_10:
assert(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов'))) == '49324 плюмбуса'

# TEST_11:
assert(choose_plural(505, ('утка', 'утки', 'уток'))) == '505 уток'

# TEST_12:
assert(choose_plural(666, ('шкаф', 'шкафа', 'шкафов'))) == '666 шкафов'

# TEST_13:
assert(choose_plural(11, ('стул', 'стула', 'стульев'))) == '11 стульев'

# TEST_14:
assert(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов'))) == '3458438435812 долларов'

# TEST_15:
assert(choose_plural(2, ('пример', 'примера', 'примеров'))) == '2 примера'

# TEST_16:
assert(choose_plural(111, ('пример', 'примера', 'примеров'))) == '111 примеров'

# TEST_17:
assert(choose_plural(1223123111, ('пример', 'примера', 'примеров'))) == '1223123111 примеров'