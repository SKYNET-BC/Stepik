en_alpha = 'abcdefghijklmnopqrstuvwxyz'
ru_alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

language = input('Выберите язык, введите - English(е)/Русский(р): ')
while language != 'е' and language != 'р':
    language = input('Доступны только команды "е" или "р": ')

text = input('Введите текст: ')  # 'Hawnj pk swhg xabkna ukq nqj.'

num = input('В каком диапазоне дешифровать: ')  #25
while not num.isdigit():
    num = input('Введите число: ')


def caesar(lang, txt, n):
    # выбор языка
    alpha = ''
    if lang == 'р':
        alpha = ru_alpha
    else:
        alpha = en_alpha

    # обработка текста
    for j in range(n):
        result = ''
        for i in txt:
            if i.isalpha():
                if i.isupper():
                    result = result + alpha[(alpha.index(i.lower()) - n) % len(alpha)].upper()
                else:
                    result = result + alpha[(alpha.index(i.lower()) - n) % len(alpha)]
            else:
                result += i
        print(result)
        n -= 1


if __name__ == '__main__':
    print(caesar(language, text, int(num)))
