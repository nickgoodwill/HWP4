# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
# 1 2 3 4 5
# 3    -> 1

n = int(input('Введите кол-во элементов: '))
some_list = []
for _ in range(n):
     some_list.append(int(input()))
print(some_list)

x = int(input('Введите число: '))
count = 0

for i in range(0, len(some_list)-1):
    if some_list[i] == x:
         count += 1

print(count)

# Задача 18: Требуется найти в списке A самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
# 1 2 3 4 5
# 6    -> 5

n = int(input('Введите кол-во элементов: '))
some_list = []
for _ in range(n):
     some_list.append(int(input()))
print(some_list)

x = int(input('Введите число: '))
index = 0
min = abs(x - some_list[0])
for i in range(1, len(some_list)-1):
    close = abs(x - some_list[i])
    if close < min:
        min = close
        index = i

print(f'Число {some_list[index]} в списке A наиболее близко по величине к числу {x}')