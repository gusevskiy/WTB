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
root.geometry('320x950+50+50')

Label(root, text = 'word')     .grid(column=0, row=0, sticky=S, pady=(5,0),padx=(2,0))
Label(root, text = 'translate').grid(column=0, row=1, sticky=S, pady=(5,0),padx=(2,0))

scroll_bar = Scrollbar(root)
scroll_bar.grid(column=3,row=4, sticky='ns')

word = Entry(root, width=20)
word.grid(column=1, row=0, columnspan = 3, sticky=S, pady=(5,0),padx=(2,0))
translate = Entry(root, width=20)
translate.grid(column=1, row=1, columnspan = 3, sticky=S, pady=(5,0),padx=(2,0))

create = Button(root, text='sort', command= sort).grid(column=0, row=2, sticky=S, pady=(5,0),padx=(2,0))
delete = Button(root, text='delete', command= delite_word).grid(column=1, row=2, sticky=S, pady=(5,0),padx=(2,0))
printW = Button(root, text='print', command= print_word).grid(column=2, row=2, sticky=S, pady=(5,0),padx=(2,0))
printW = Button(root, text='save', command= save_word).grid(column=3, row=2, sticky=S, pady=(5,0),padx=(2,0))
a = Button(root, text='a', height=1, width=1, command= save_word).grid(column=5, row=0, sticky=S, pady=(5,0),padx=(2,0))
b = Button(root, text='b', height=1, width=1, command= save_word).grid(column=5, row=1, sticky=S, pady=(5,0),padx=(2,0))
c = Button(root, text='c', height=1, width=1, command= save_word).grid(column=5, row=2, sticky=S, pady=(5,0),padx=(2,0))
d = Button(root, text='d', height=1, width=1, command= save_word).grid(column=5, row=3, sticky=S, pady=(5,0),padx=(2,0))
e = Button(root, text='e', height=1, width=1, command= save_word).grid(column=5, row=4, sticky=S, pady=(5,0),padx=(2,0))
f = Button(root, text='f', height=1, width=1, command= save_word).grid(column=5, row=5, sticky=S, pady=(5,0),padx=(2,0))
g = Button(root, text='g', height=1, width=1, command= save_word).grid(column=5, row=6, sticky=S, pady=(5,0),padx=(2,0))
h = Button(root, text='h', height=1, width=1, command= save_word).grid(column=5, row=7, sticky=S, pady=(5,0),padx=(2,0))
i = Button(root, text='i', height=1, width=1, command= save_word).grid(column=5, row=8, sticky=S, pady=(5,0),padx=(2,0))
j = Button(root, text='j', height=1, width=1, command= save_word).grid(column=5, row=9, sticky=S, pady=(5,0),padx=(2,0))
k = Button(root, text='k', height=1, width=1, command= save_word).grid(column=5, row=10, sticky=S, pady=(5,0),padx=(2,0))
l = Button(root, text='l', height=1, width=1, command= save_word).grid(column=5, row=11, sticky=S, pady=(5,0),padx=(2,0))
m = Button(root, text='m', height=1, width=1, command= save_word).grid(column=5, row=12, sticky=S, pady=(5,0),padx=(2,0))
n = Button(root, text='n', height=1, width=1, command= save_word).grid(column=5, row=13, sticky=S, pady=(5,0),padx=(2,0))
o = Button(root, text='o', height=1, width=1, command= save_word).grid(column=5, row=14, sticky=S, pady=(5,0),padx=(2,0))
p = Button(root, text='p', height=1, width=1, command= save_word).grid(column=5, row=15, sticky=S, pady=(5,0),padx=(2,0))
q = Button(root, text='q', height=1, width=1, command= save_word).grid(column=5, row=16, sticky=S, pady=(5,0),padx=(2,0))
r = Button(root, text='r', height=1, width=1, command= save_word).grid(column=5, row=17, sticky=S, pady=(5,0),padx=(2,0))
s = Button(root, text='s', height=1, width=1, command= save_word).grid(column=5, row=18, sticky=S, pady=(5,0),padx=(2,0))
t = Button(root, text='t', height=1, width=1, command= save_word).grid(column=5, row=19, sticky=S, pady=(5,0),padx=(2,0))
u = Button(root, text='u', height=1, width=1, command= save_word).grid(column=5, row=20, sticky=S, pady=(5,0),padx=(2,0))
v = Button(root, text='v', height=1, width=1, command= save_word).grid(column=5, row=21, sticky=S, pady=(5,0),padx=(2,0))
w = Button(root, text='w', height=1, width=1, command= save_word).grid(column=5, row=22, sticky=S, pady=(5,0),padx=(2,0))
x = Button(root, text='x', height=1, width=1, command= save_word).grid(column=5, row=23, sticky=S, pady=(5,0),padx=(2,0))
y = Button(root, text='y', height=1, width=1, command= save_word).grid(column=5, row=24, sticky=S, pady=(5,0),padx=(2,0))
z = Button(root, text='z', height=1, width=1, command= save_word).grid(column=5, row=25, sticky=S, pady=(5,0),padx=(2,0))


list_word = Listbox(root, height=45, width=30, selectmode=EXTENDED)
list_word.grid(column=0, row=3, columnspan=4, rowspan=23, sticky=S, pady=(5,0),padx=(2,0))
list_word.config(yscrollcommand = scroll_bar.set)
scroll_bar.config(command=list_word.yview)


root.mainloop()
