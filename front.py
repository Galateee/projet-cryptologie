import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
from tkinter import simpledialog
import bcrypt

from DBInterraction import create_dictionary, connection_dictionary, create_key, get_passwords, add_password, delete_password, update_password

current_dictionary_id = None
current_key = None

def login_to_safe():
    global current_dictionary_id, current_key

    password = simpledialog.askstring("Connexion", "Entrez le mot de passe du coffre-fort :", show="*")
    if not password:
        return

    dictionary_id = connection_dictionary(password)
    if dictionary_id:
        current_dictionary_id = dictionary_id
        current_key = create_key()
        messagebox.showinfo("Succès", "Connexion réussie !")
        show_safe_page()
    else:
        messagebox.showerror("Erreur", "Mot de passe incorrect.")

def create_new_safe():
    global current_dictionary_id, current_key

    password = simpledialog.askstring("Création", "Entrez un mot de passe pour le nouveau coffre-fort :", show="*")
    if not password:
        return

    dictionary_id = create_dictionary(password)
    current_dictionary_id = dictionary_id
    current_key = create_key()
    messagebox.showinfo("Succès", "Nouveau coffre-fort créé avec succès !")
    show_safe_page()

def display_passwords():
    if current_dictionary_id is None:
        messagebox.showerror("Erreur", "Vous devez d'abord vous connecter.")
        return

    passwords = get_passwords(current_dictionary_id, current_key)
    popup = tk.Toplevel()
    popup.title("Mots de passe enregistrés")

    for subject, password in passwords:
        tk.Label(popup, text=f"Sujet : {subject} | Mot de passe : {password}").pack()

def add_new_password():
    if current_dictionary_id is None:
        messagebox.showerror("Erreur", "Vous devez d'abord vous connecter.")
        return

    def save_password():
        subject = subject_entry.get()
        password = password_entry.get()
        if not subject or not password:
            messagebox.showwarning("Attention", "Tous les champs doivent être remplis.")
            return

        add_password(current_dictionary_id, current_key, password, subject)
        messagebox.showinfo("Succès", "Mot de passe ajouté avec succès !")
        popup.destroy()

    popup = tk.Toplevel()
    popup.title("Ajouter un mot de passe")
    tk.Label(popup, text="Sujet :").pack(pady=5)
    subject_entry = tk.Entry(popup)
    subject_entry.pack(pady=5)
    tk.Label(popup, text="Mot de passe :").pack(pady=5)
    password_entry = tk.Entry(popup, show="*")
    password_entry.pack(pady=5)
    tk.Button(popup, text="Enregistrer", command=save_password).pack(pady=10)

def delete_password_popup():
    if current_dictionary_id is None:
        messagebox.showerror("Erreur", "Vous devez d'abord vous connecter.")
        return

    def confirm_deletion():
        subject = subject_entry.get()
        if not subject:
            messagebox.showwarning("Attention", "Le champ Sujet est vide.")
            return

        delete_password(current_dictionary_id, subject)
        messagebox.showinfo("Succès", f"Mot de passe pour '{subject}' supprimé avec succès.")
        popup.destroy()

    popup = tk.Toplevel()
    popup.title("Supprimer un mot de passe")
    tk.Label(popup, text="Sujet à supprimer :").pack(pady=5)
    subject_entry = tk.Entry(popup)
    subject_entry.pack(pady=5)
    tk.Button(popup, text="Supprimer", command=confirm_deletion).pack(pady=10)

def update_password_popup():
    if current_dictionary_id is None:
        messagebox.showerror("Erreur", "Vous devez d'abord vous connecter.")
        return

    def confirm_update():
        subject = subject_entry.get()
        new_password = new_password_entry.get()
        if not subject or not new_password:
            messagebox.showwarning("Attention", "Tous les champs doivent être remplis.")
            return

        update_password(current_dictionary_id, current_key, subject, new_password)
        messagebox.showinfo("Succès", f"Mot de passe pour '{subject}' mis à jour avec succès.")
        popup.destroy()

    popup = tk.Toplevel()
    popup.title("Mettre à jour un mot de passe")
    tk.Label(popup, text="Sujet :").pack(pady=5)
    subject_entry = tk.Entry(popup)
    subject_entry.pack(pady=5)
    tk.Label(popup, text="Nouveau mot de passe :").pack(pady=5)
    new_password_entry = tk.Entry(popup, show="*")
    new_password_entry.pack(pady=5)
    tk.Button(popup, text="Mettre à jour", command=confirm_update).pack(pady=10)

def show_safe_page():
    main_frame.pack_forget()
    safe_frame.pack(fill="both", expand=True, padx=10, pady=10)

def show_main_page():
    safe_frame.pack_forget()
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

root = tk.Tk()
root.title("Gestionnaire de mot de passe")
root.geometry("1000x600")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

tk.Label(main_frame, text="Bienvenue dans le gestionnaire de mots de passe", font=("Helvetica", 16)).pack(pady=20)

tk.Button(main_frame, text="Se connecter", command=login_to_safe).pack(pady=10)
tk.Button(main_frame, text="Créer un nouveau coffre-fort", command=create_new_safe).pack(pady=10)

safe_frame = tk.Frame(root)

tk.Label(safe_frame, text="Coffre-fort", font=("Helvetica", 16)).pack(pady=20)
tk.Button(safe_frame, text="Afficher les mots de passe", command=display_passwords).pack(pady=10)
tk.Button(safe_frame, text="Ajouter un mot de passe", command=add_new_password).pack(pady=10)
tk.Button(safe_frame, text="Supprimer un mot de passe", command=delete_password_popup).pack(pady=10)
tk.Button(safe_frame, text="Mettre à jour un mot de passe", command=update_password_popup).pack(pady=10)
tk.Button(safe_frame, text="Déconnexion", command=show_main_page).pack(pady=20)

root.mainloop()


