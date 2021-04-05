#   -----------------------------------------------------------
#
#   Вычислить плошадь и периметр правильного 17-угольника,
#   вписанного в  окружность заданного радиуса
#
#   Copyright (c) 2021. Danil Smirnov
#   Released under GNU Public License (GPL)
#   email zabanen.nu@ya.ru
#   -----------------------------------------------------------
import math


def get_polygon_area(radius, edges=17):
    return ((edges / 2) * radius ** 2) * math.sin((2 * math.pi) / edges)


def get_polygon_perimeter(radius, edges=17):
    angle = 360 / edges
    return math.sqrt((radius ** 2) * 2 - (2 * (radius * radius)) * math.cos(angle))


radius = int(input('Введите радиус окружности:\n'))

print('Площадь правильного 17 угольника вписанного в окружность:')
print(get_polygon_area(radius))
print('Периметр правильного 17 угольника вписанного в окружность:')
print(get_polygon_perimeter(radius))
