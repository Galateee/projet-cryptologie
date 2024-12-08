from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256

import bcrypt
import base64

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
    print("le mot de passe ne correspond à aucun coffre fort")
    return False

def create_key():
    return Fernet.generate_key()

def get_passwords(currentDictionaryId, key):

    Database.cursor.execute("SELECT encrypted_password, subject FROM Passwords WHERE id_dictionary = (?)", (currentDictionaryId,))
    rows = Database.cursor.fetchall()

    for row in rows:
        print("--------")
        print("sujet :", row[1])
        print("mot de passe :", Fernet(key).decrypt(row[0].decode()).decode('utf-8'))
        print("--------\n")

def add_password(currentDictionaryId, key, password, subject):
   
    encryptedPassword = Fernet(key).encrypt(password.encode())
    Database.cursor.execute("INSERT INTO Passwords (encrypted_password, subject, id_dictionary) VALUES (?, ?, ?)", (encryptedPassword, subject, currentDictionaryId))
    Database.connection.commit()

def delete_password(currentDictionaryId, subject):
    Database.cursor.execute("DELETE FROM Passwords WHERE subject = (?) AND id_dictionary = (?)", (subject, currentDictionaryId))
    Database.connection.commit()

def update_password(currentDictionaryId, key, subject, newPw):
    newCryptedPw = Fernet(key).encrypt(newPw.encode())
    Database.cursor.execute("UPDATE Passwords SET encrypted_password = (?) WHERE id_dictionary = (?) AND subject = (?)", (newCryptedPw, currentDictionaryId, subject))
    Database.connection.commit()