while True:
    try:
        a = int(input('введите первое число:'))
        b = int(input('введите второе число:'))
        print("разность чисел: ", a-b)
        break
    except:
        print("Ошибка! Вводить нужно числа!")