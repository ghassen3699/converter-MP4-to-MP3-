

# le choix de l'utilisateur
###########################################################################
def choix_utilsiateur () :
    print("VOUS VOULLEZ CONVERTIR DES AUTRES FICHIERS ")
    print("1) OUI ")
    print("2) NON ")

    test = False
    while test == False :
        while True :
            try:
                choix = int(input("---> "))
                break
            except ValueError :
                print("ERREUR ENTRER UN ENTIER 1 OU 2")

        if choix == 1 or choix == 2 :
            test = True
        else:
            test = False
    return choix
############################################################################
