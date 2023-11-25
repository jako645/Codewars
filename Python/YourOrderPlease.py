import re

def order(sentence):
    ordered_list = [None] * len(sentence.split())

    for word in sentence.split():
        no = int(((re.findall('[1-9]', word)))[0])

        ordered_list[no - 1] = word
    
    return ' '.join(ordered_list)
