import json
from difflib import get_close_matches

data = json.load(open('data.json'))
data = dict(zip(map(str.lower,data.keys()),data.values()))

def get_meaning(word):
    word = word.lower()
    try:
        meaning = data[word]
        display(meaning)
    except KeyError:
        probable_word = get_close_matches(word, data.keys())
        if len(probable_word) > 0:
            yn = input('Do you mean: %s \nEnter Y for yes, or N for no : '%probable_word[0])
            if yn in'Yy':
                meaning = data[probable_word[0]]
                display(meaning)
            elif yn in 'Nn':
                print("Word doesn't exist. Please check the spelling.")
            else:
                print("We don't understand the word.")
        else:
            print("Word does't exist. Please check for spelling errors.")


def display(meaning):
    for i in range(len(meaning)):
        print(i+1,".", meaning[i])


word=input("Enter word : ")
get_meaning(word)