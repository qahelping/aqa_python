"""
Примеры некоторых стандартных итерабельных объектов.
Пример 1: список
"""

# Список
my_list = [1, 2, 5, 7, 32, 148]

# Обход списка
for element in my_list:
    print(element)

# Функция enumerate возвращает итерабельный объект, который возвращает пары индекс-значение
for index, element in enumerate(my_list):
    print('my_list[{}] = {}'.format(index, element))




"""
Примеры некоторых стандартных итерабельных объектов.
Пример 2: строка
"""

# Строка
string = 'A string'

# Обход строки посимвольно
for char in string:
    print(char)


# Пример генератора
def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5):
    print(i, end = ' : ')


x = gensquares(4)
print(x)
print(next(x))
print(next(x))
print(next(x))
print(next(x))



try:
    x = 2 / 0
except ZeroDivisionError:
    print('Division by zero detected')



def add_values(a, b):
    return a + b

try:
    add_values(4, '5')
except TypeError:
    print('Bad arguments')

try:
    2 / 0
finally:
    print('Finally block is always executed')




class MyException(Exception):
    pass

try:
    raise MyException("error")
except Exception:
    print('some exception')
except MyException as e:
    print(e)
