from tkinter import *


def print_word():
    list_word.delete(0, END)
    file = open("word_translate.txt", "r", encoding="utf-8")
    for i in file:
        list_word.insert(END, i)
        
def one():
    infile = open('word_translate.txt', 'r', encoding="utf-8") 
    outfile = open('sort_word_translate.txt', 'w', encoding="utf-8")
    lines = []
    for l in infile:
        lines.append(l.strip()+'\n')
    lines.sort()
    outfile.writelines(lines)
    infile.close()
    outfile.close()
    
def tu():
    outfile = open('sort_word_translate.txt', 'r', encoding="utf-8")
    infile = open('word_translate.txt', 'w', encoding='utf-8')
    for i in outfile:
        infile.write(i)
    infile.close()
    outfile.close()
    
def sort():
    one()
    tu()
    
def save_word():
    w = word.get()
    t = translate.get()
    wt = w + '-' + t
    f = open('word_translate.txt', 'a', encoding='utf-8')
    f.writelines('\n'+wt)
    f.close()
    clear_entry()
    print_word()

def delite_word():
    del_word = list(list_word.curselection())
    del_word.reverse()
    for i in del_word:
        list_word.delete(i)
    f = open('word_translate.txt', 'w', encoding='utf-8')
    f.writelines((list_word.get(0,END)))
    f.close()

def clear_entry():
    word.delete(0, END)
    translate.delete(0, END)
    
        
root = Tk()
root.title('dictionary WTB')
root.geometry('200x500+50+50')


Label(root, text = 'word')     .grid(column=0, row=0, sticky=S, pady=(5,0),padx=(2,0))
Label(root, text = 'translate').grid(column=0, row=1, sticky=S, pady=(5,0),padx=(2,0))

word = Entry(root, width=20)
word.grid(column=1, row=0, columnspan = 3, sticky=S, pady=(5,0),padx=(2,0))
translate = Entry(root, width=20)
translate.grid(column=1, row=1, columnspan = 3, sticky=S, pady=(5,0),padx=(2,0))

create = Button(root, text='sort', command= sort).grid(column=0, row=2, sticky=S, pady=(5,0),padx=(2,0))
delete = Button(root, text='delete', command= delite_word).grid(column=1, row=2, sticky=S, pady=(5,0),padx=(2,0))
printW = Button(root, text='print', command= print_word).grid(column=2, row=2, sticky=S, pady=(5,0),padx=(2,0))
printW = Button(root, text='save', command= save_word).grid(column=3, row=2, sticky=S, pady=(5,0),padx=(2,0))


list_word = Listbox(root, height=30, width=30, selectmode=EXTENDED)

list_word.grid(column=0, row=4, columnspan=4, sticky=S, pady=(5,0),padx=(2,0))


root.mainloop()
