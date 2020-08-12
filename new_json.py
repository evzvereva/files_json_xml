import json
from collections import Counter

with open('newsafr.json', encoding='utf-8') as f:
    file_json = json.load(f)

list_elem = []
for key in file_json['rss']['channel']['items']:
    value = key['description'].split()
    for elem in value:
        list_elem.append(elem)

dictionary_news = {}
for key_words, count_repetitions in dict(Counter(sorted(list_elem))).items():
    if len(key_words) > 6:
        dictionary_news[key_words] = count_repetitions

for x in Counter.most_common(dictionary_news, 10):
    print(f'Слово "{list(x)[0]}" повторяется {list(x)[1]} раз')
