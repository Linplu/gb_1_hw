# 1
# def sum_digits(num):
#     return sum(map(int, num.replace('.','').replace('-','')))
#
# num = input('Введите любое вещественное число: ')
# print(f'Сумма цифр в этом числе равна {sum_digits(num)}')

# 2
# N = int(input('Введите число '))
#
# f = 1
# for i in range(N):
#     i = i + 1
#     f = i * f
#
#     print(f, end=" ")

# 3
# n = int(input('Введите количество чисел в списке '))
#
# def numbers(n):
#     summ = 0
#     for i in range(n):
#         a = int(input(f'Введи число {i + 1} '))
#         a = (1+1/a)**a
#         summ = a + summ
#         i += 1
#     return summ
#
# print('Сумма чисел равна',round((numbers(n)), 2))
