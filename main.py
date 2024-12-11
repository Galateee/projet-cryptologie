import DBInterraction

currentDictionaryId = False
antiBrutForce = 0

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
        else:
            currentDictionaryId = DBInterraction.create_dictionary(pw)
            key = DBInterraction.create_key()
            print("voici votre clé confidentielle pour accéder à vos mots de passes, veuillez la concerver précieusement :")
            print(key.decode('utf-8'))  #pour enlever les charactères b'' autour de la clé
    elif choice == "2":
        pw = input("Entrez le mot de passe du coffre : ")
        currentDictionaryId = DBInterraction.connection_dictionary(pw) #retourne false si aucun mot de passe ne correspond
        key = input("veuillez saisir votre clé confidentielle pour permettre le déchiffrage de vos mots de passes : ")
    elif choice == "q":
        print ("Bye")
        exit()
    else :
        print("Invalid choice!")

    if currentDictionaryId != False :
        DioctionaryConnexion = True

    if antiBrutForce >= 5:
        print("trop d'essais raté, veuillez relancer l'application") #défence contre les attaques brut force
        exit()
    antiBrutForce+=1

print("\nconnexion au coffre fort") 

Actions = False
while Actions == False: #action dans le coffre fort

    print("""What do you want to do ?
    (1) Voir mes mots de passe
    (2) Ajouter un mot de passe
    (3) Supprimer un mot de passe
    (4) Editer un mot de passe
    (5) changer la clé confidentielle saisie
    (6) Exporter votre coffre fort
    (q) Quit
    """)

    choice = input("enter your choice: ")
    if choice == "1":
        DBInterraction.get_passwords(currentDictionaryId, key)
    elif choice == "2":
        subject = input("pour quel sujet voulez vous créer un mot de passe ? : ")
        newPassword = input("ajoutez un mot de passe : ")
        DBInterraction.add_password(currentDictionaryId, key, newPassword, subject)
    elif choice == "3":
        subject = input("indiquez le sujet du mot de passe à supprimer : ")
        DBInterraction.delete_password(currentDictionaryId, subject)
        print("le mot de passe à été supprimé\n")
    elif choice == "4":
        subject = input("indiquez le sujet du mot de passe à modifier : ")
        newPw = input("indiquez le nouveau mot de passe : ")
        DBInterraction.update_password(currentDictionaryId, key, subject, newPw)
        print("le mot de passe à été supprimé\n")
    elif choice == "5":
        key = input("veuillez saisir votre clé confidentielle afin de déchiffrer vos mots de passes")
    elif choice == "6":
        print("ouais exportation")
    elif choice == "q":
        print ("Bye")
        exit()
    else :
        print("Invalid choice!")