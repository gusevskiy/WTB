from tkinter import *


def print_word():
    list_word.delete(0, END)
    file = open("word_translate.txt", "r", encoding="utf-8")
    for i in file:
        list_word.insert(END, i)
        
# add words in db    
def add():
    list = []
    with open('word_translate.txt', 'r', encoding='utf-8') as file:
        data = file.read().splitlines()
        data.sort()
        for i in data:
            list.append(i)
    w = word.get()
    t = translate.get()
    list.append(w+'-'+t)
    list.sort()
    with open('word_translate.txt', 'w', encoding='utf-8') as file:
        for i in list:
            file.write(i+'\n')
    print_word()
    clear_entry()
  
def clear_entry():
    word.delete(0, END)
    translate.delete(0, END)
  

def delite_word():
    with open('word_translate.txt', 'w', encoding='utf-8') as file:
        file.writelines('\n'.join(list_word.get(0, END)))
           
    # del_word = list_word.curselection()
    # list_word.delete(del_word[0])
    # data = list_word
    # print(data)
    # with open('word_translate.txt', 'w', encoding='utf-8') as file:
    #     file.writelines(data)
        
  

root = Tk()
root.title('dictionary WTB')
root.geometry('300x300+50+50')


Label(root, text = 'word')     .grid(column=0, row=0, sticky=S, pady=(5,0),padx=(2,0))
Label(root, text = 'translate').grid(column=0, row=1, sticky=S, pady=(5,0),padx=(2,0))

word = Entry(root, width=20)
word.grid(column=1, row=0, columnspan = 3, sticky=S, pady=(5,0),padx=(2,0))
translate = Entry(root, width=20)
translate.grid(column=1, row=1, columnspan = 3, sticky=S, pady=(5,0),padx=(2,0))

create = Button(root, text='add', command= add).grid(column=0, row=2, sticky=S, pady=(5,0),padx=(2,0))
delete = Button(root, text='delete', command= delite_word).grid(column=1, row=2, sticky=S, pady=(5,0),padx=(2,0))
printW = Button(root, text='print', command= print_word).grid(column=2, row=2, columnspan=3, sticky=S, pady=(5,0),padx=(2,0))


list_word = Listbox(root, height=30, width=30)

list_word.grid(column=0, row=4, columnspan=4, sticky=S, pady=(5,0),padx=(2,0))


root.mainloop()
