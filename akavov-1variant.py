from math import sqrt
from time import time

def vremya(func):
    def timeFunc(*args):
        start = time()
        func(*args)
        print(f'Время работы функции: {time() - start}')
    return timeFunc

def decorat(func):
    def name(*args):
        print(f'Была вызвана функция: {func.__name__}')
        func(*args)
    return name

@vremya
@decorat
def square(a, b):
    print(f'Площадь участка равна {round(a * b / 43560, 6)} акров')

@vremya
@decorat
def freeFall(h):
    vf = sqrt(0 ** 2 + 2 * 9.8 * h)
    print(f'Скорость при приземлении равна {vf} м/c')


a, b = int(input('Введите длину: ')), int(input('Введите ширину: '))
square(a, b)
h = int(input('Сколько метров высота падения? '))
freeFall(h)