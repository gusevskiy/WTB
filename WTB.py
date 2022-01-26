from tkinter import *


def print_word():
    list_word.delete(0, END)
    file = open("word_translate.txt", "r", encoding="utf-8")
    for i in file:
        list_word.insert(END, i)
        
def add():
    w = word.get()
    t = translate.get()
    wt = w + '-' + t
    list_word.insert(END, wt)
    clear_entry()
    sort()
         
def sort():
    infile = open('sort_word_translate.txt', 'r', encoding='utf-8')
    outfile = open('word_translate.txt', 'w', newline='', encoding='utf-8')
    list = []
    for i in infile:
        list.append(i.strip()+'\n')
    list.sort()
    outfile.writelines(list)
    infile.close()
    outfile.close()
    print(list)
    
def save_word():
    f = open('sort_word_translate.txt', 'w', encoding='utf-8')
    f.writelines(list_word.get(0, END))
    f.close()
  
def clear_entry():
    word.delete(0, END)
    translate.delete(0, END)
  

def delite_word():
    del_word = list(list_word.curselection())
    del_word.reverse()
    for i in del_word:
        list_word.delete(i)
    
        
root = Tk()
root.title('dictionary WTB')
root.geometry('200x400+50+50')


Label(root, text = 'word')     .grid(column=0, row=0, sticky=S, pady=(5,0),padx=(2,0))
Label(root, text = 'translate').grid(column=0, row=1, sticky=S, pady=(5,0),padx=(2,0))

word = Entry(root, width=20)
word.grid(column=1, row=0, columnspan = 3, sticky=S, pady=(5,0),padx=(2,0))
translate = Entry(root, width=20)
translate.grid(column=1, row=1, columnspan = 3, sticky=S, pady=(5,0),padx=(2,0))

create = Button(root, text='add', command= add).grid(column=0, row=2, sticky=S, pady=(5,0),padx=(2,0))
delete = Button(root, text='delete', command= delite_word).grid(column=1, row=2, sticky=S, pady=(5,0),padx=(2,0))
printW = Button(root, text='print', command= print_word).grid(column=2, row=2, sticky=S, pady=(5,0),padx=(2,0))
printW = Button(root, text='save', command= save_word).grid(column=3, row=2, sticky=S, pady=(5,0),padx=(2,0))


list_word = Listbox(root, height=30, width=30, selectmode=EXTENDED)

list_word.grid(column=0, row=4, columnspan=4, sticky=S, pady=(5,0),padx=(2,0))


root.mainloop()
