from random import choice


digits = '1234567890'
low_letters = 'qwertyuiopasdfghjklzxcvbnm'
upp_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
symbols = '!#$%&*+-=?@^_'
chars = ''

n = int(input('Количество паролей для генерации: '))
len = int(input('Длина пароля: '))

def generate_pwd(length, chars):
    pwd = ''
    for _ in range(length):
        pwd += choice(chars)
    return pwd


incld_dig = input('Включать ли фицры? Да/Нет: ')
if incld_dig in ('Да','да'):
    chars += digits
incld_upp_lett = input('Включать ли буквы верхнего регистра? Да/Нет: ')
if incld_upp_lett in ('Да','да'):
    chars += upp_letters
incld_low_lett = input('Включать ли буквы нижнего регистра? Да/Нет: ')
if incld_low_lett in ('Да','да'):
    chars += low_letters
incld_symb = input('Включать ли спецсимволы? Да/Нет: ')
if incld_symb in ('Да','да'):
    chars += symbols
excld_symb = input('Исключить неоднозначные символы il1Lo0O? Да/Нет: ')
if excld_symb in ('Да','да'):
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

for _ in range(n):
    print(generate_pwd(len, chars))
