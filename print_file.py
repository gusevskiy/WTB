with open('word_translate.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
del data[0]

with open('word_translate.txt', 'w', encoding='utf-8') as file:
    file.writelines(data)