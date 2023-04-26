from tkinter import (
    ANCHOR, E, END, SINGLE, W, S,
    Button, Entry, Label, Listbox, Scrollbar, Tk
)


def print_word():
    if letter.get() == '':
        # sort()
        list_word.delete(0, END)
        with open("word_translate.txt", "r", encoding="utf-8") as file:
            for i in file:
                list_word.insert(END, i)
    else:
        list_word.delete(0, END)
        let = letter.get()
        with open('word_translate.txt', 'r', encoding='utf-8') as file:
            for i in file:
                if i.startswith(let):  # если строка в файле начинается на let вывод ее в list_word т.е. на экран
                    list_word.insert(END, i)
        letter.delete(0, END)


def save_word():
    if word.get() == '' and translate.get() == '':
        print_word()
        return None
    
    else:
        words = []
        with open('word_translate.txt', 'r', encoding='utf-8') as f:
            for i in f:
                words.append(i)
        w = word.get()
        t = translate.get()
        wt = w + ' - ' + t
        words.append(wt+'\n')
        words.sort()
        with open('word_translate.txt', 'w', encoding='utf-8') as f:
            for i in words:
                f.write(i)
        clear_entry()
        print_word()


def delite_word():
    word = list_word.get(ANCHOR)
    sd = []
    with open('word_translate.txt', 'r', encoding='utf-8') as f:
        for i in f:
            sd.append(i)
    sd.remove(word)
    with open('word_translate.txt', 'w', encoding='utf-8') as f:
        for i in sd:
            f.write(i)
    print_word()


def del_keyboard(self):  # функция специально для кнопки Delete
    delite_word()


def enter_perform(self):  # функция специально для кнопки Enter
    save_word()    


def clear_entry():
    word.delete(0, END)
    translate.delete(0, END)
    
        
root = Tk()
root.title('dictionary WTB')
root.geometry('400x650+50+50')

Label(root, text='word').grid(
    column=0, row=0, sticky=S, pady=(5, 0), padx=(2, 0)
)
Label(root, text='translate').grid(
    column=0, row=1, sticky=S, pady=(5, 0), padx=(2, 0)
)
Label(root, text='search').grid(
    column=0, row=2, sticky=S, pady=(5, 0), padx=(2, 0)
)

scroll_bar = Scrollbar(root)
scroll_bar.grid(column=3, row=3, sticky='ns')

word = Entry(root, width=36)
word.grid(column=1, row=0, sticky=W, pady=(5, 0), padx=(2, 0))
translate = Entry(root, width=36)
translate.grid(column=1, row=1, sticky=W, pady=(5, 0), padx=(2, 0))
letter = Entry(root, width=10)
letter.grid(column=1, row=2, sticky=W, pady=(5, 0), padx=(2, 0))

save_bottom = Button(
    root, text='perform', command=save_word, height=1, width=20
)
save_bottom.grid(column=1, row=2, sticky=E, pady=(5, 0), padx=(2, 0))

root.bind('<Delete>', del_keyboard)
root.bind('<Return>', enter_perform)

list_word = Listbox(
    root, height=25, width=45,
    selectmode=SINGLE, selectborderwidth=2,
    font=('Consolas', '9')
)
list_word.grid(
    column=0, row=3, columnspan=2, pady=1, padx=1, ipadx=1, ipady=1
)
list_word.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_word.yview)


root.mainloop()
