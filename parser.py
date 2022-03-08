import pandas as pd

def parse(filepath, source, target):
    source_path = "./diff_lang_keyword/{}_python_keyword.csv".format(source)
    target_path = "./diff_lang_keyword/{}_python_keyword.csv".format(target)
    python_source = pd.read_csv(source_path)
    python_target = pd.read_csv(target_path)
    source_keys = python_source["Words"].tolist()
    target_keys = python_target["Words"].tolist()
    with open(filepath, 'r') as file :
        filedata = file.read()

    for word in len(range(source_keys)):
        # Replace the target string
        filedata = filedata.replace(source_keys, target_keys)

    # Write the file out again
    with open(filepath, 'w') as file:
        file.write(filedata)

def main():
    source_lang = input("Lang of source file")
    source_path = input("Path of source file")
    target_lang = input("Lang of target file")
    parse(source_path, source_lang, target_lang)
    print("File Translated")

main()