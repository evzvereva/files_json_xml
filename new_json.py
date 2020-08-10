import json
from collections import defaultdict
from collections import Counter

counter = defaultdict(int)

with open('newsafr.json', encoding='utf-8') as f:
    file_json = json.load(f)

for key in file_json['rss']['channel']['items']:
    value = key['description'].split()
    for elem in value:
        counter[elem] += 1
        dups = {e: count for e, count in counter.items()}

sorted_keys = sorted(dups, key=dups.get, reverse=True)

dictionary = {}

for keys in sorted_keys:
    if len(keys) > 6:
        dictionary[keys] = dups[keys]

vocabulary_list = Counter.most_common(dictionary, 10)

for final_value in vocabulary_list:
    print(f'Слово "{final_value[0]}" повторяется {final_value[1]} раз')
