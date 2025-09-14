'''Ahora  conoceremos un poco sqllite
    1- Crearemos una base de datos.
    2. Definiremos una tabla sencilla.
    3. la guardaremos en una DB.
    4. consultaremos nuestra tabla.
'''
import sqlite3
from typing import List, Dict, Tuple

def main(db_name: str,  records: List[Tuple]):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS users")
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            age INTEGER
        )
    ''')
    ## insert values
    formatted__values = ','.join(
        [f"('{name}', '{surname}', {age})"
         for name, surname, age in records]
        )
    print(formatted__values)
    cursor.execute(f"INSERT INTO users (name, surname, age) VALUES {formatted__values}")
    ## Select all
    cursor.execute("SELECT *  FROM users; ")
    query_results = cursor.fetchall()
    print('All users', query_results)
    ## 
    cursor.execute("SELECT name, surname, age  FROM users ORDER BY age DESC LIMIT 1; ")
    query_results = cursor.fetchall()
    print(f'Oldest user: {query_results}')

if __name__ == '__main__':
    users = [('Alice', 'Robert', 30),
             ('Mark', 'Jackson', 50), 
             ('Matt', 'Williams', 23)]
    main(db_name='social_media.db', records=users)
    
