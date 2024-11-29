import tkinter as tk

root = tk.Tk()
root.title("Mon Application ")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

left_frame = tk.Frame(main_frame, bg="lightblue", width=300)
left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

right_frame = tk.Frame(main_frame, bg="lightgray", width=300)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

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

def access_my_new_safe():
    mot_de_passe_1 = text_input1.get("1.0", tk.END).strip() 
    mot_de_passe_2 = text_input2.get("1.0", tk.END).strip()  

    if mot_de_passe_1 == mot_de_passe_2 and mot_de_passe_1 != "":
        print("Coffre-fort ouvert")
    else:
        print("Coffre-fort fermé : les mots de passe ne correspondent pas ou sont vides")


access_button = tk.Button(left_frame, text="Accédez à mon coffre-fort", command=access_my_new_safe)
access_button.pack(pady=10)



access_label = tk.Label(right_frame, text="Coffre-fort existant", bg="lightgray", font=("Helvetica", 14))
access_label.pack(pady=10)

entry = tk.Entry(right_frame, show="*")
entry.pack(pady=5)

def access_my_safe():
    valeur = entry.get()  
    if valeur == "1234":  
        print("Coffre-fort ouvert")
    else:
        print("Mot de passe incorrect")

access_button = tk.Button(right_frame, text="Accédez à mon coffre-fort", command=access_my_safe)
access_button.pack(pady=10)

root.mainloop()
