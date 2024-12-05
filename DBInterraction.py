from cryptography.fernet import Fernet
import bcrypt

import Database

def create_dictionary(password):

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) #Hash du mot de passe mis en base

    Database.cursor.execute("INSERT INTO Dictionary (dictionary_password) VALUES (?)", (hashed_password,))

    Database.connection.commit()

    return Database.cursor.lastrowid # retourne l'id de la ligne créée
    
def connection_dictionary(password):

    Database.cursor.execute("SELECT dictionary_id, dictionary_password FROM Dictionary")
    rows = Database.cursor.fetchall()

    for row in rows:
        if bcrypt.checkpw(password.encode('utf-8'), row[1]): #comparer chaque mot de passe hashé en base avec le paramètre
            return row[0]    

def create_key():
    return Fernet.generate_key()
