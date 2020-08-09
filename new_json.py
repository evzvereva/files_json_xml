import json
from collections import defaultdict
from collections import OrderedDict

counter = defaultdict(int)

with open('newsafr.json', encoding='utf-8') as f:
    file_json = json.load(f)


new_list = file_json['rss']['channel']['items']

for new in new_list:
    list_news = new['description'].split() + new['title'].split()
    for elem in list_news:
        counter[elem] += 1
        dups = {e: count for e, count in counter.items() if count > 0}

sorted_keys = sorted(dups, key=dups.get, reverse=True)

dictionary = {}

for keys in sorted_keys:
    if len(keys) > 6:
        dictionary[keys] = dups[keys]

output = OrderedDict()

for key, value in dictionary.items():
    if key not in output:
        output[key] = value
        if len(output) == 10:
            break

for final_key, final_value in output.items():
    print(f'Слово "{final_key}" повторяется {final_value} раз')
