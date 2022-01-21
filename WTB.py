
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
        print(value[0], '-', value[1])
        
print_word()

# add words in db    
def add():
    word = input()
    translate = input()
    
    cur.execute("SELECT word FROM words;")
    rows = cur.fetchall()
    if (word,) in rows:
        print('Такая запись уже есть!')
    else:
        cur.execute(f'''INSERT INTO words (word, translate) VALUES ('{word}', '{translate}');''')
        con.commit()
        print(f"A word has been added to the word table, {word}")
add()
       
  
# Delete word  
# def delite_word():
#     cur.execute("DELETE FROM words WHERE id = (SELECT MAX(id) FROM words);")
#     print('Delete word')
#     con.commit()
    




# con.close()