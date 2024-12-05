import tkinter as tk

def show_safe_page():
    """Affiche la page du coffre-fort."""
    main_frame.pack_forget()

    clear_frame(safe_frame)

    safe_frame.pack(fill="both", expand=True, padx=10, pady=10)

    label = tk.Label(safe_frame, text="Bienvenue dans votre coffre-fort", font=("Helvetica", 16), bg="lightgreen")
    label.pack(pady=20)

    button_frame = tk.Frame(safe_frame)
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Ajouter un nouveau mot de passe", command=add_new_mdp)
    add_button.pack(side="left", padx=10)

    delete_button = tk.Button(button_frame, text="Supprimer un mot de passe", command=delete_mdp)
    delete_button.pack(side="right", padx=10)

    edit_button = tk.Button(button_frame, text="Modifier un mot de passe", command=edit_mdp)
    edit_button.pack(padx=10)

    export_coffre_button = tk.Button(button_frame, text="Exporter mon coffre-fort", command=export_coffre)
    export_coffre_button.pack(pady=20)

    back_button = tk.Button(safe_frame, text="Retour", command=show_main_page)
    back_button.pack(pady=20)


def clear_frame(frame):
    """Supprime tous les widgets."""
    for widget in frame.winfo_children():
        widget.destroy()


def add_new_mdp():
    """Ajoute un nouveau mot de passe."""
    safe_frame.pack_forget()

    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

def delete_mdp():
    """Supprime un mot de passe."""
    safe_frame.pack_forget()

    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

def edit_mdp():
    """Modifier un mot de passe."""
    safe_frame.pack_forget()

    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

def export_coffre():
    """Exporter le coffre-fort."""
    safe_frame.pack_forget()

    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

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

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

left_frame = tk.Frame(main_frame, bg="lightblue", width=300)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

title_label = tk.Label(left_frame, text="Créer mon coffre-fort", font=("Helvetica", 16), bg="lightblue")
title_label.pack(pady=10)

frame = tk.Frame(left_frame, bg="lightblue")
frame.pack(pady=10)

label1 = tk.Label(frame, text="Nouveau Mot de passe", bg="lightblue")
label1.grid(row=1, column=0, padx=5, pady=5, sticky="e")
text_input1 = tk.Text(frame, height=2, width=30)
text_input1.grid(row=1, column=1, padx=5, pady=5)

label2 = tk.Label(frame, text="Confirmer le même mot de passe", bg="lightblue")
label2.grid(row=2, column=0, padx=5, pady=5, sticky="e")
text_input2 = tk.Text(frame, height=2, width=30)
text_input2.grid(row=2, column=1, padx=5, pady=5)

access_button = tk.Button(left_frame, text="Accédez à mon coffre-fort", command=access_my_new_safe)
access_button.pack(pady=10)

error_label = tk.Label(left_frame, text="", bg="lightblue", fg="red")
error_label.pack()

right_frame = tk.Frame(main_frame, bg="lightgray", width=300)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

access_label = tk.Label(right_frame, text="Coffre-fort existant", bg="lightgray", font=("Helvetica", 14))
access_label.pack(pady=10)

entry = tk.Entry(right_frame, show="*")
entry.pack(pady=5)

access_button_right = tk.Button(right_frame, text="Accédez à mon coffre-fort", command=access_my_safe)
access_button_right.pack(pady=10)

error_label_right = tk.Label(right_frame, text="", bg="lightgray", fg="red")
error_label_right.pack()

safe_frame = tk.Frame(root, bg="lightgreen")

root.mainloop()
