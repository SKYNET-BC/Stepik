en_alpha = 'abcdefghijklmnopqrstuvwxyz'
ru_alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

action = input('Выберите действие, введите букву - шифровать(ш)/дешифровать(д): ')
while action != 'ш' and action != 'д':
    action = input('Доступны только команды "ш" или "д": ')

language = input('Выберите язык, введите - English(е)/Русский(р): ')
while language != 'е' and language != 'р':
    language = input('Доступны только команды "е" или "р": ')

step = input('Сдвиг символов на: ')
while not step.isdigit():
    step = input('Введите число: ')

text = input('Введите текст: ')


def caesar(act, lang, stp, txt):
    # сдвиг влево (дешифрование) / вправо (шифрование)
    if act == 'д':
        stp = int('-' + stp)
    else:
        stp = int(stp)

    # выбор языка
    alpha = ''
    if lang == 'р':
        alpha = ru_alpha
    else:
        alpha = en_alpha

    # обработка текста
    result = ''
    for i in txt:
        if i.isalpha():
            if i.isupper():
                result = result + alpha[(alpha.index(i.lower()) + stp) % len(alpha)].upper()
            else:
                result = result + alpha[(alpha.index(i.lower()) + stp) % len(alpha)]
        else:
            result += i
    return result


if __name__ == '__main__':
    print(caesar(action, language, step, text))
