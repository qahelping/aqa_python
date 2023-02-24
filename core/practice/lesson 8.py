

current = 0
previous = 1

n = 10

print(current, previous, end=' ')

for i in range(0, n - 1):
    current, previous = previous, current + previous
    print(previous, end=' ')

print('-------------------------------')


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for i in range(11):
    print(next(gen), end=' ')

print('-------------------------------')

def fib_list(n, current=0, previous=1, result=[0]):
    if n == 0:
        return result
    else:
        result.append(current + previous)
        return fib_list(n - 1, current + previous, current, result)


print(*fib_list(10))

print('-------------------------------')

def decorator(func):
    def wrapper(arg1, arg2):
        func(arg1, arg2)
    return wrapper

@decorator
def print_full_name(first_name, last_name):
    print("My name is", first_name, last_name)

print_full_name("Ivan", "Ivanou")

print('-------------------------------')

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    print()
    return 'всем привет'


print(say_hi())

print('-------------------------------')

import requests
def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@benchmark
def fetch_webpage():
    webpage = requests.get('https://www.google.ru/')
    print(webpage)


fetch_webpage()

print('-------------------------------')

from functools import wraps

def fake(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("{} was faked".format(func.__name__))
        return None

    return inner

@fake
def power(a: int, b: int) -> int:
    """
        Calculates the power for the base a and exp - b
        a: int
        b: int
        return: int
    """
    return a ** b

a = power()
print(a)

print("Name", power.__name__)
print("Annotations", power.__annotations__)
print("Documentation", power.__doc__)


print('-------------------------------')

def multiply(num1): # внешняя функция
   var = 10 # не запомним это значение
   def inner(num2): # замыкание
       return num1 * num2
   return inner

print(multiply(4))
# <function multiply.<locals>.inner at 0x100418550>
print(multiply(4)(5))  # 20

func = multiply(4)
print(func(6))  # 24


print('-------------------------------')

import requests
import time

def time_req(func):

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)

    return wrapper()

@time_req
def test_req():
    requests.get('https://www.google.ru/?hl=ru')



class MyException(Exception):
    pass


def tooy(kind):
    def inner(color):
        try:
            if kind == 'Медведики' and color == 'желтый':
                raise MyException('error')
            else:
                print(f'Игрушка - {kind}, Цвет - {color}')
        except MyException as e:
            pass

    return inner


a = tooy('Мячик')  # конвеер мячиков
b = tooy('Куклы')  # конвеер кукол
c = tooy('Медведики')  # конвеер медведиков

a('красный')
a('синий')
a('желтый')

b('красный')
b('синий')
b('желтый')

c('красный')
c('синий')
c('желтый')