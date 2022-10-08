# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('\n' * 100)
quarter = int(input('Введите номер четверти координатной плоскости '))
print('\n')
if quarter == 1:
    print('X > 0 и Y > 0')
    print('\n')
else:
    if quarter == 2:
        print('X < 0 и Y > 0')
        print('\n')
    else:
        if quarter == 3:
            print('X < 0 и Y < 0')
            print('\n')
        else:
            if quarter == 4:
                print('X > 0 и Y < 0')
                print('\n')
            else:
                print('Стопэ!!! У нас всего 4 четверти!!!')
                print('\n')
