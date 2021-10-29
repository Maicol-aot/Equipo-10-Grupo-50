import sqlite3
from sqlite3 import Error
from flask import g

def get_db(): 
    try: 
        if 'db' not in g: 
            print('conectado')
            db = sqlite3.connect('database.db')
        return db 
    except Error: 
        print(Error)

def close_db():
     if db is not None: 
         db.close()