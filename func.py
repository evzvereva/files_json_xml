from collections import Counter


def filter_words_6_letters(words):
    return [word for word in words if len(word) > 6]


def count_words(words):
    return Counter(words)


def popular_words(words):
    return Counter.most_common(words, 10)


def print_result(list_words):
    for words in list_words:
        print(f'Слово "{words[0]}" повторяется {words[1]} раз')
