from random import choice
from time import sleep


def magic():
    magic_list = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
        'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
        'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
        'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
        'Перспективы не очень хорошие', 'Весьма сомнительно']
    return choice(magic_list)

def another_question(quest):
    if quest in ('Да', 'да'):
        return True
    elif quest in ('Нет', 'нет'):
        return False
    else:
        return another_question(input('Пожалуйста, введите "Да" или "Нет": '))


def start():
    while True:
        question = input('Введите ваш вопрос: ')
        answer = magic()
        print('Нужно подумать..')
        sleep(5)
        print(answer)
        sleep(5)
        if another_question(input('Желаете задать еще вопрос? Да/Нет: ')):
            continue
        else:
            print('Возвращайтесь, когда появятся вопросы!')
            break


start()