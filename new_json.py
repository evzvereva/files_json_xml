import json
import func

with open('newsafr.json', encoding='utf-8') as f:
    file_json = json.load(f)

list_elem = []
for key in file_json['rss']['channel']['items']:
    value = key['description'].split()
    for elem in value:
        list_elem.append(elem)

filtered_words = func.filter_words_6_letters(list_elem)
counted_words = func.count_words(filtered_words)
result_popular_words = func.popular_words(counted_words)
func.print_result(result_popular_words)
