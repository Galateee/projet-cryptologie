import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet


# Classe PasswordManager
class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password_file(self, path, initial_values=None):
        self.password_file = path
        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file = path
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site, password):
        self.password_dict[site] = password
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict.get(site, "Mot de passe introuvable")


# Application Tkinter
def show_safe_page():
    """Affiche la page du coffre-fort."""
    main_frame.pack_forget()  
    safe_frame.pack(fill="both", expand=True, padx=10, pady=10) 

    label = tk.Label(safe_frame, text="Bienvenue dans votre coffre-fort", font=("Helvetica", 16), bg="lightgreen")
    label.pack(pady=20)

    button_frame = tk.Frame(safe_frame)
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Ajouter un nouveau mot de passe", command=add_new_mdp)
    add_button.pack(side="left", padx=10)

    delete_button = tk.Button(button_frame, text="Afficher un mot de passe", command=view_mdp)
    delete_button.pack(side="right", padx=10)

    export_coffre_button = tk.Button(button_frame, text="Charger un fichier", command=load_password_file)
    export_coffre_button.pack(pady=20)

    back_button = tk.Button(safe_frame, text="Retour", command=show_main_page)
    back_button.pack(pady=20)


def clear_frame(frame):
    """Supprime tous les widgets."""
    for widget in frame.winfo_children():
        widget.destroy()


def add_new_mdp():
    """Ajoute un nouveau mot de passe."""
    def save_password():
        site = site_entry.get()
        password = password_entry.get()
        if site and password:
            manager.add_password(site, password)
            messagebox.showinfo("Succès", f"Mot de passe ajouté pour {site}.")
            popup.destroy()
        else:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs.")

    popup = tk.Toplevel()
    popup.title("Ajouter un mot de passe")
    tk.Label(popup, text="Site :").grid(row=0, column=0, padx=10, pady=10)
    site_entry = tk.Entry(popup)
    site_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(popup, text="Mot de passe :").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(popup, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(popup, text="Enregistrer", command=save_password).grid(row=2, column=0, columnspan=2, pady=10)


def view_mdp():
    """Afficher un mot de passe."""
    def search_password():
        site = site_entry.get()
        if site:
            password = manager.get_password(site)
            result_label.config(text=f"Mot de passe pour {site} : {password}")

    popup = tk.Toplevel()
    popup.title("Afficher un mot de passe")
    tk.Label(popup, text="Site :").grid(row=0, column=0, padx=10, pady=10)
    site_entry = tk.Entry(popup)
    site_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Button(popup, text="Rechercher", command=search_password).grid(row=1, column=0, columnspan=2, pady=10)
    result_label = tk.Label(popup, text="", fg="blue")
    result_label.grid(row=2, column=0, columnspan=2, pady=10)


def load_password_file():
    """Charger un fichier de mots de passe."""
    path = filedialog.askopenfilename(title="Charger un fichier de mots de passe", filetypes=[("Fichiers texte", "*.txt")])
    if path:
        try:
            manager.load_password_file(path)
            messagebox.showinfo("Succès", "Fichier chargé avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement du fichier : {e}")


def show_main_page():
    """Retourne à la page principale."""
    safe_frame.pack_forget()  
    main_frame.pack(fill="both", expand=True, padx=10, pady=10) 


def access_my_new_safe():
    mot_de_passe_1 = text_input1.get("1.0", tk.END).strip()
    mot_de_passe_2 = text_input2.get("1.0", tk.END).strip()
    if mot_de_passe_1 == mot_de_passe_2 and mot_de_passe_1 != "":
        show_safe_page()
    else:
        error_label.config(text="Erreur : Les mots de passe ne correspondent pas ou sont vides.")


def access_my_safe():
    """Vérifie si le mot de passe du coffre-fort est correct."""
    valeur = entry.get()
    if valeur == "1234":
        show_safe_page()
    else:
        error_label_right.config(text="Mot de passe incorrect.")


root = tk.Tk()
root.title("Mon Application ")
root.geometry("1200x800")
manager = PasswordManager() 

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

left_frame = tk.Frame(main_frame, bg="lightblue", width=300)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

right_frame = tk.Frame(main_frame, bg="lightgray", width=300)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

safe_frame = tk.Frame(root, bg="lightgreen")

text_input1 = tk.Text(main_frame, height=1, width=20)
text_input1.pack(pady=10)
text_input2 = tk.Text(main_frame, height=1, width=20)
text_input2.pack(pady=10)

error_label = tk.Label(main_frame, fg="red")
error_label.pack(pady=10)

login_button = tk.Button(main_frame, text="Se connecter", command=access_my_new_safe)
login_button.pack(pady=20)

back_button = tk.Button(main_frame, text="Retour", command=show_main_page)
back_button.pack(pady=20)

root.mainloop()
