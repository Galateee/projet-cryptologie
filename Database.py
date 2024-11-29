import sqlite3

connection = sqlite3.connect("password_db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Dictionary(
    dictionary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dictionary_password TEXT NOT NULL)
    """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS Password (
    password_id INTEGER PRIMARY KEY AUTOINCREMENT,
    encrypted_password TEXT NOT NULL,
    id_dictionary INTEGER,
    FOREIGN KEY (id_dictionary) REFERENCES Dictionary(dictionary_id))
    """)

connection.commit()