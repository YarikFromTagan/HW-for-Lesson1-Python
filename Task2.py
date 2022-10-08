# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('\n' * 100)

for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f'для X = {x}, Y = {y}, Z = {z}')
                print(f'выражение - {not (x or y or z) == (not x and not y and not z)}')
                




