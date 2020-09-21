from PyDictionary import PyDictionary
import json

lang_code = json.load(open('languagecode.json'))

word = input('Enter the word : ')
dictionary=PyDictionary(word)

def translate_word():
    lang = input('Enter the language in which you want the translation : ')
    if lang.capitalize() not in lang_code.keys():
        print("Not a valid language selection")
    print(dictionary.translate(word, lang_code[lang.capitalize()]))


def get_result(choice):
    try:
        switcher={
            '1':dictionary.printMeanings(),
            '2':dictionary.printSynonyms(),
            '3':dictionary.printAntonyms(),
            '4':translate_word()
        }
        return switcher.get(choice,'Invalid Selection')
    except:
        return "Word doesn't exist. Check for spelling errors."

print('Press:\n1: Meaning\n2: Synonyms\n3: Antonyms\n4: Translate')
choice = input()


print(get_result(choice))