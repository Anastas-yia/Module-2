my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
while count < len(my_list):
    number = my_list[count]
    count = count + 1
    if number < 0:
        break
    elif number == 0:
        continue
    else:
        print(number)