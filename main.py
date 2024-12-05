import DBInterraction

currentDictionaryId = False

DioctionaryConnexion = False

while DioctionaryConnexion == False: #connexion au coffre fort

    print("""What do you want to do ?
      (1) Créer un coffre fort
      (2) Charger un coffre fort
      (q) Quit
      """)
        
    choice = input("enter your choice: ")
    if choice == "1":
        pw = input("Entrez le mot de passe du coffre : ")
        pw2 = input("Entrez le mot de passe une seconde fois : ")
        if pw != pw2:
            print("les mots de passes sont différents")
            exit
        else:
            currentDictionaryId = DBInterraction.create_dictionary(pw)
    elif choice == "2":
        pw = input("Entrez le mot de passe du coffre : ")
        currentDictionaryId = DBInterraction.connection_dictionary(pw)
    elif choice == "q":
        DioctionaryConnexion = True
        print ("Bye")
    else :
        print("Invalid choice!")

    if currentDictionaryId != False :
        DioctionaryConnexion = True

    print("connexion au coffre fort")
        

Actions = False

while Actions == False: #action dans le coffre fort

    print("""What do you want to do ?
    (1) Voir mes mots de passe
    (2) Ajouter un mot de passe
    (3) Supprimer un mot de passe
    (4) Editer un mot de passe
    (5) Exporter votre coffre fort
    (q) Quit
    """)

    choice = input("enter your choice: ")
    if choice == "1":
        a
    elif choice == "2":
        a
    elif choice == "3":
        a
    elif choice == "4":
        a
    elif choice == "5":
        print("ouais exportation")
    elif choice == "q":
        Actions = True
        print ("Bye")
    else :
        print("Invalid choice!")