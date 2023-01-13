import sqlite3

conn = sqlite3.connect('todos.db')
cursor = conn.cursor()

cursor.execute(
    f'CREATE TABLE users (id int, username varchar(255), password text)')
cursor.execute(f'CREATE TABLE lists (id int, user_id int, name varchar(255))')
cursor.execute(
    f'CREATE TABLE todos (id int, user_id int, list_id int, content text, status int)')
cursor.execute(
    f'CREATE TABLE statuses (id int, user_id int, title varchar(64))')
