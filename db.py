import sqlite3

db = sqlite3.connect('database.db')
cur = db.cursor()


# добавление элемента в БД
def add_element(name_program: str, URL: str):
    cur.execute(f'INSERT INTO db VALUES (?, ?)', (name_program, URL))
    db.commit()


# удаление элемента из БД
def del_element(name_program: str):
    cur.execute(f"DELETE FROM db WHERE name_program = '{name_program}'")
    db.commit()


# поиск элемента в БД по ключу
def find_element(name_program: str):
    for i in cur.execute('SELECT * FROM db'):
        if i[0] == name_program:
            return i[1]
