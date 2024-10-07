print('Задача "Все ли равны?"')
First = int(input('Введите первое число '))
Second = int(input('Введите второе число '))
Third = int(input('Введите третье число '))
if First == Second and First == Third:
   print(3)
elif First == Second or First == Third or Second == Third:
   print(2)
else: print(0)