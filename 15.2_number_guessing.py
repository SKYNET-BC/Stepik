'''Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100 и просит пользователя угадать это число.
Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.
Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.'''
import random


#  получаем случайное число
def get_num():
    global max_val  # используется в функции is_valid
    max_val = input('Введите значение. Загаданное число будет в диапазоне от 1 до: ')
    return random.randint(1, int(max_val))


#  проверяем, что введено число, в соответствующем диапазоне
def is_valid(num):
    while True:
        if not num.isdigit() or not 1 <= int(num) <= int(max_val):
            num = input('Должно быть введено число от 1 до ' + max_val + ', попробуйте еще раз: ')
        elif num.isdigit() and 1 <= int(num) <= int(max_val):
            break
    return int(num)


#  продолжаем игру?
def continue_game():
    answer = input('Желаете повторить? y(да) / n(нет): ')
    while True:
        if answer not in ('y', 'n'):
            answer = input('Для ответа принимаются только буквы "y" и "n". Желаете повторить? y(да) / n(нет): ')
        if answer == 'y':
            return True
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            return False


#  игра
def game():
    print('Добро пожаловать в числовую угадайку')
    while True:
        number = get_num()
        #  print('Загаданное число:', number) #  отладка
        #  ввод первого предполагаемого числа
        n = is_valid(input('Угадайте загаданное число, ваш вариант: '))
        #  счетчик попыток
        counter = 1
        #  запускаем цикл угадывания
        while n != number:
            if n > number:
                n = is_valid(input('Слишком много, попробуйте еще раз: '))
                counter += 1
                continue
            else:
                n = is_valid(input('Слишком мало, попробуйте еще раз: '))
                counter += 1
                continue
        if n == number:
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', counter)
        if continue_game():
            continue
        else:
            break


game()
