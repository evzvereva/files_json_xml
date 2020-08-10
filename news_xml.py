import xml.etree.ElementTree as ET
from collections import defaultdict
from collections import OrderedDict

counter = defaultdict(int)

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

channel_node = root.find('channel')

items_list_description = root.findall('channel/item/description')

for news in items_list_description:
    for elem in news.text.split():
        counter[elem] += 1
        dups = {e: count for e, count in counter.items()}

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
