import xml.etree.ElementTree as ET
from collections import defaultdict
import func

counter = defaultdict(int)

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

channel_node = root.find('channel')

items_list_description = root.findall('channel/item/description')

list_words = []
for news in items_list_description:
    for elem in news.text.split():
        list_words.append(elem)

filtered_words = func.filter_words_6_letters(list_words)
counted_words = func.count_words(filtered_words)
result_popular_words = func.popular_words(counted_words)
func.print_result(result_popular_words)
