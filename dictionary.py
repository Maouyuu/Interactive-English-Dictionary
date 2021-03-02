import json
from difflib import get_close_matches


dictionary = json.load(open(r'C:\Users\Ilyas\github\Interactive-English-Dictionary\data.json'))


def get_def(word):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    close_matches = get_close_matches(word, dictionary.keys())
    if len(close_matches) > 0:
        # best_match = max([[w, SequenceMatcher(None, word, w).ratio()] for w in dictionary.keys()], key=lambda x: x[1])[0]
        if input(f'Do you mean {close_matches[0]} ? Y/N') == 'Y':
            return dictionary[close_matches[0]]
        else:
            return ['We could not find your word.Please reverify it']
    return ['Inexistant word']


word = input('Please enter a word:')


print(*get_def(word), sep='\n')
