import random

def num_cipher():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    cipher = random.choice(numbers)
    return cipher

num_1 = num_cipher()
print('На первом камне выпало число: ', num_1)

num_1_user = int(input('Введите число, выпавшее на камне: '))

result = []
if num_1_user == num_1:
    for i in range(1, 20):
        for j in range(1, i):
            if num_1_user % (i + j) == 0:
                result.append(i)
                result.append(j)
                answer = True
                if num_1_user % (i + j) != 0:
                    answer = False
    print('Этот набор цифр спасет вам жизнь: ', *result)
else:
    print('Посмотрите внимательнее на камень! Там другое число!')
