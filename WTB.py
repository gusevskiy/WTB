from tkinter import *


def print_word():
    if letter.get() == '':
        sort()
        list_word.delete(0, END)
        with open("word_translate.txt", "r", encoding="utf-8") as file:
            for i in file:
                list_word.insert(END, i)
    else:
        list_word.delete(0,END)
        let = letter.get()
        with open('word_translate.txt', 'r', encoding='utf-8') as file:
            for i in file:
                if i.startswith(let):
                    list_word.insert(END, i)
        letter.delete(0, END)
        
        
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
    if word.get() == '' and translate.get() == '':
        return None
    else:
        w = word.get()
        t = translate.get()
        wt = w + ' - ' + t
        f = open('word_translate.txt', 'a', encoding='utf-8')
        f.writelines(wt)
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
    
def del_keyboard(self):# функция специально для кнопки Delete
    delite_word()

def clear_entry():
    word.delete(0, END)
    translate.delete(0, END)
    
        
root = Tk()
root.title('dictionary WTB')
root.geometry('280x750+50+50')

Label(root, text = 'word')     .grid(column=0, row=0, sticky=S, pady=(5,0),padx=(2,0))
Label(root, text = 'translate').grid(column=0, row=1, sticky=S, pady=(5,0),padx=(2,0))

scroll_bar = Scrollbar(root)
scroll_bar.grid(column=3,row=3, sticky='ns')

word = Entry(root, width=30)
word.grid(column=1, row=0, sticky=S, pady=(5,0),padx=(2,0))
translate = Entry(root, width=30)
translate.grid(column=1, row=1, sticky=S, pady=(5,0),padx=(2,0))
letter = Entry(root, width=2)
letter.grid(column=1, row=2, pady=(5,0),padx=(2,0))

print_bottum = Button(root, text='print', command= print_word, height=1, width=8)
print_bottum.grid(column=1, row=2, sticky=E, pady=(5,0),padx=(2,0))
save_bottom = Button(root, text='save', command= save_word, height=1, width=8)
save_bottom.grid(column=1, row=2, sticky=W, pady=(5,0),padx=(2,0))

root.bind('<Delete>', del_keyboard)

list_word = Listbox(root, height=40, width=42, selectmode=SINGLE)
list_word.grid(column=0, row=3, columnspan=2, pady=(5,0),padx=(2,0))
list_word.config(yscrollcommand = scroll_bar.set)
scroll_bar.config(command=list_word.yview)


root.mainloop()
