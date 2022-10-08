# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

import os
os.system('cls')
quarter = int(input('Введите номер четверти координатной плоскости '))
print('\n')
if quarter == 1:
    print('X > 0 и Y > 0')
    print('\n')
elif quarter == 2:
    print('X < 0 и Y > 0')
    print('\n')
elif quarter == 3:
    print('X < 0 и Y < 0')
    print('\n')
elif quarter == 4:
    print('X > 0 и Y < 0')
    print('\n')
else:
    print('Стопэ!!! У нас всего 4 четверти!!!')
    print('\n')
