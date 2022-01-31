a = input()
str(a)
with open('word.txt', 'r', encoding='utf-8') as file:
    for i in file:
        if i.startswith(f'{a}'):
            print(i.strip())