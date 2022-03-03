import googletrans
from googletrans import * 
from google_trans_new import google_translator
import csv

py_keys = []

with open('python_keyword.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    fields = next(file)
    for row in csvFile:
        py_keys.append(row)


all_lang = googletrans.LANGUAGES


# for adding to a csv file

for key in all_lang:
    lang = all_lang[key]
    name_file = lang + '_python_keyword.csv'

    with open(name_file, 'w') as new_file:
        writer = csv.writer(new_file)
        header_tag = "List of all Python Keywords in " + lang
        header = [header_tag]
        writer.writerow(header)

        for word in py_keys:
            py_key = word[0]
            translator = google_translator()  
            translate_text = translator.translate(py_key, lang_tgt = key)
            translate_text_arr = []
            translate_text_arr.append(translate_text)
            writer.writerow(translate_text_arr)
        


#for adding to a txt file

# for key in all_lang:
#     lang = all_lang[key]
#     name_file = lang + '_python_keyword.txt'
#     new_file = open(name_file,'w')

#     for word in py_keys:
#         py_key = word[0]
#         translator = google_translator()  
#         translate_text = translator.translate(py_key, lang_tgt = key)
#         new_file.write(translate_text)
#         new_file.write("\n")
    
#     new_file.close()
