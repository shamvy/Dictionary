import json
from PyDictionary import PyDictionary

lang_code = json.load(open('languagecode.json'))
word = input('Enter the word : ')
dictionary=PyDictionary(word)

def translate_word():
    lang = input('Enter the language in which you want the translation : ')
    if lang.capitalize() not in lang_code.keys():
        print("Not a valid language selection")
    print(dictionary.translate(word, lang_code[lang.capitalize()]))

translate_word()
