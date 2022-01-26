# with open('word_translate.txt', 'r', encoding='utf-8') as file:
#     data = file.readlines()
# del data[0]

# with open('word_translate.txt', 'w', encoding='utf-8') as file:
#     file.writelines(data)

infile = open('word.txt', 'r')  # Файл с мусором
outfile = open('sortedlines.txt', 'w', newline='')  # "Очищенный" файл
lines = []
for l in infile:
    lines.append(l.strip()+'\n')
lines.sort()
outfile.writelines(lines)
infile.close()
outfile.close()