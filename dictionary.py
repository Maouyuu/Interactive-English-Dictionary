import json
from difflib import get_close_matches


dictionary = json.load(open(r'C:\Users\Ilyas\github\Interactive-English-Dictionary\data.json'))


def is_proper_noun(word):
    if word[0] >= 'A' and word[0] <= 'Z' and word[1:] == word[1:].lower():
        return True
    return False


def get_def(word):
    if not is_proper_noun(word):
        word = word.lower()
    if word in dictionary:
        return dictionary[word]
    close_matches = get_close_matches(word, dictionary.keys())
    close_matches_proper = get_close_matches(word[0].upper() + word[:], dictionary.keys())
    if len(close_matches) > 0:
        # best_match = max([[w, SequenceMatcher(None, word, w).ratio()] for w in dictionary.keys()], key=lambda x: x[1])[0]
        if input(f'Do you mean {close_matches[0]} ? Y/N') == 'Y':
            return dictionary[close_matches[0]]
        elif input(f'Do you mean {close_matches_proper[0]} ? Y/N') == 'Y':
            return dictionary[close_matches_proper[0]]
        return ['We could not find your word.Please reverify it']
    return ['Inexistant word']


word = input('Please enter a word:')


print(*get_def(word), sep='\n')
