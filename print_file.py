# with open('word_translate.txt', 'r', encoding='utf-8') as file:
#     data = file.readlines()
# del data[0]

# with open('word_translate.txt', 'w', encoding='utf-8') as file:
#     file.writelines(data)
def one():
    infile = open('word.txt', 'r')  # Файл с мусором
    outfile = open('sortedlines.txt', 'w')  # "Очищенный" файл
    lines = []
    for l in infile:
        lines.append(l.strip()+'\n')
    lines.sort()
    outfile.writelines(lines)
    infile.close()
    outfile.close()
    
def tu():
    outfile = open('sortedlines.txt', 'r')
    infile = open('word.txt', 'w')
    for i in outfile:
        infile.write(i)
    infile.close()
    outfile.close()
    
one()
tu()