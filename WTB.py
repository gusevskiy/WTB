from cProfile import label
from cgitb import text
from tkinter import *
import sqlite3




# connect db
try:
    con = sqlite3.connect('translateWord.db')
    table_db = '''CREATE TABLE IF NOT EXISTS words (
                        id integer primary key AUTOINCREMENT,
                        word varchar(50),
                        translate varchar(50));'''                 
    cur = con.cursor()
    print("Connected to DB translateWord")
    cur.execute(table_db)
    con.commit()
    
except sqlite3.Error as error:
    print('Error connect!')


def print_word():
    print("В базе имеются такие слова")
    for value in cur.execute("SELECT word, translate FROM words;"):
        translate_word.insert(1.0, value, '/n') 
        
        


# add words in db    
def add():
    try:
        w = word.get()
        t = translate.get()
        
        cur.execute("SELECT word FROM words;")
        rows = cur.fetchall()
        if (word,) in rows:
            print('Такая запись уже есть!')
        else:
            cur.execute(f'''INSERT INTO words (word, translate) VALUES ('{w}', '{t}');''')
            con.commit()
            print(f"A word has been added to the word table, {w}")
            clear_entry()
    except:
        return None

def clear_entry():
    word.delete(0, END)
    translate.delete(0, END)
  
#Delete word  
def delite_word():
    cur.execute("DELETE FROM words WHERE id = (SELECT MAX(id) FROM words);")
    print('Delete word')
    con.commit()
    
# con.close()

root = Tk()
root.title('dictionary WTB')
root.geometry('300x300+50+50')


Label(root, text = 'word')     .grid(column=0, row=0, sticky=S, pady=(5,0),padx=(2,0))
Label(root, text = 'translate').grid(column=0, row=1, sticky=S, pady=(5,0),padx=(2,0))

word = Entry(root, width=20)
word.grid(column=1, row=0, columnspan = 3, sticky=S, pady=(5,0),padx=(2,0))
translate = Entry(root, width=20)
translate.grid(column=1, row=1, columnspan = 3, sticky=S, pady=(5,0),padx=(2,0))

create = Button(root, text='save', command= add).grid(column=0, row=2, sticky=S, pady=(5,0),padx=(2,0))
delete = Button(root, text='delete', command= delite_word).grid(column=1, row=2, sticky=S, pady=(5,0),padx=(2,0))
printW = Button(root, text='print', command= print_word).grid(column=2, row=2, columnspan=3, sticky=S, pady=(5,0),padx=(2,0))

translate_word = Text(root, height=30, width=30)
translate_word.grid(column=0, row=4, columnspan=4, sticky=S, pady=(5,0),padx=(2,0))


root.mainloop()
