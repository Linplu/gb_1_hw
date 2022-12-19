# 1
# x = [2, 3, 6, 10, 12, 16, 5]
# summ = 0
# for i in range(1, len(x), 2):
#         summ += x[i]
# print(f"{x} -> сумма элементов на нечётных позициях: {summ}")
# 2
# from random import randint
#
# number = int(input('Введите размер списка '))
# list = []
# list2 = []
# for i in range(number):
#     list.append(randint(0, 9))
# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1
# print(list)
# print(list2)

# 3
# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))