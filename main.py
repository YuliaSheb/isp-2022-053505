import re
from statistics import median


def osnova():
    file = open('text.txt', 'r')
    text = file.read()
    file.close()
    words = re.findall('[a-zа-яё]+', text, re.I)
    print(words)
    dicts = {}
    for word in words:
        count = dicts.get(word, 0)
        dicts[word] = count + 1

    dict_keys = dicts.keys()

    for word in dict_keys:
        print(word, dicts[word])

    sent = re.sub(r'[.!?]\s', r' | ', text)
    number_sent = len(sent.split(' | '))
    mean_number_sent = len(text.split()) / number_sent

    print(sent)
    print('В этом тексте {} предложения'.format(number_sent))
    print('Среднее количество слов в предложении: ', round(mean_number_sent, 4))
    print("Количество слов в предложении :", len(words))
    print("Медианное количество слов в предложении = ", median([len(re.findall(r'\b\w{1,15}\b', sentence)) for sentence
                                                                in sent.split(' | ')]))


def dop():
    file = open('text.txt', 'r')
    text = file.read()
    file.close()
    while 1:
        print("Если хотите ввести K и N самостоятельно, нажмите 1. В противном случае нажмите 2")
        numb = int(input())
        if numb == 1:
           print("Введите значение K: ")
           k = int(input())
           print("Введите значение N: ")
           n = input()
           break

        elif numb == 2:
           k = 10
           n = '4'
           break

    else:
        print("Введенно некоректное значение")

    words = re.findall(r'\b\w{'+n+'}\\b', text)

    dict = {}

    for word in words:
        count = dict.get(word, 0)
        dict[word] = count + 1

    dict_item = list(dict.items())
    dict_item.sort(key=lambda i: i[1])
    dict_item.reverse()

    counter = 0
    while counter < k and counter != len(dict.items()):
        print(dict_item[counter])
        counter += 1


def main():
   osnova()
   dop()


main()
