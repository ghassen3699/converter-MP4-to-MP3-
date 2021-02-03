
if __name__ == '__main__':
    import convertisseur
    import fichier_utilisateur
    test = False
    print("------------------------------- BIENVENUE -----------------------------")

    while test == False :
        convertisseur.convertisseur()
        choix = fichier_utilisateur.choix_utilsiateur()
        if choix == 1 :
            test = False
        else:
            test = True
            print("---------------------------------- AU REVOIR ------------------------------------")