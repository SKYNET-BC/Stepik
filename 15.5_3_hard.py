alpha = 'abcdefghijklmnopqrstuvwxyz'

text = [i for i in input('Введите текст: ').split()]


def len_of_line(word):
    counter = 0
    for i in word:
        if i.isalpha():
            counter += 1
    return counter


def caesar(txt):
    # обработка текста
    result = []
    for i in txt:
        line = i
        new_line = ''
        stp = len_of_line(line)
        for j in line:
            if j.isalpha():
                if j.isupper():
                    new_line = new_line + alpha[(alpha.index(j.lower()) + stp) % len(alpha)].upper()
                else:
                    new_line = new_line + alpha[(alpha.index(j.lower()) + stp) % len(alpha)]
            else:
                new_line += j
        result.append(new_line)
    return result


if __name__ == '__main__':
    print(*caesar(text))
