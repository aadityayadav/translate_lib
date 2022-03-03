import googletrans
from googletrans import * 
# from googletrans import Translator


translator = googletrans.Translator()

key_file = open('python_keyword.txt', 'r')
Lines = key_file.readlines()

all_lang = googletrans.LANGUAGES


for key in all_lang:
    lang = all_lang[key]
    name_file = lang + '_python_keyword.txt'
    new_file = open(name_file,'w')

    for word in Lines:
        py_key = word
        translate = translator.translate(py_key, dest = lang)
        new_file.write(translate.text)
    
    new_file.close()
