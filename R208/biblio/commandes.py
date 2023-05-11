"""chemin pour l'environement python3"""
#!/usr/bin/env python3

from biblio.livre import Livre


# --- Fonctions d'affichage ---

def afficher_menu():
    """Affichage du menu"""
    phrase2 = "\n Menu principale \n"
    phrase_option = " [M] Menu Principal \n [LG] Listes des Genres "
    phrase3 = "\n [LL] Listes des livres \n [NG] Nouveau Genre \n [NL] Nouveau Livre"
    phrase_option2 = " [SG] Suppression Genres \n [SL] Suppresion Livres"
    phrase_fin = "\n [Q] Quitter le programme"
    print("*" * 40 + phrase2 + phrase_option + phrase3 )
    print(phrase_option2 + phrase_fin + "\n" + "*" * 40)


def affiche_livre(biblio):
    """Affichage de la liste des livres"""
    biblio.afficher_livre()


def affiche_genre(biblio):
    """Affichage de la liste des genres """
    biblio.afficher_genre()


# --- Fonctions d'ajout ---

def nouveau_genre(biblio):
    """Fonction qui ajoute un genre saisi par l'utilisateur"""
    genre_question = str(input(">Entrez le nom du genre : "))
    # appel la méthode genre existe de la classe bibliotheque qui va revoyer une valeur booléenne
    rep = biblio.genre_existe(genre_question)
    if rep:
        print(">Le genre existe déjà.")
    else:
        biblio.genre_ajout(genre_question)  # ajout du genre
    return genre_question #renvoie le genre saisie


def nouveaux_livre(biblio):
    """Fonction qui ajoute dans la bibliothèque un livre ajouté par l'utilisateur"""
    titre_livre = str(input(">Entrez le titre: "))
    genre_livre = str(input(">Entrez le genre: "))
    annee_livre = int(input(">Entrez l'année de parution: "))
    if annee_livre > 2023:  # Verifie que la date saisie n'est pas superieur à la date actuel
        print("Mauvaise saisie de la date")
        annee_livre = int(input(">Entrez l'année de parution: "))
    rep = biblio.genre_existe(genre_livre)  # Verification du genre saisi
    if rep:  # si le genre est déjà repertorié, on ajoute simplement le livre
        livre = Livre(titre_livre, annee_livre, genre_livre)
        biblio.livre_ajout(livre)  # ajout du livre dans la bibliothèque
        print("Le livre", titre_livre, "a été ajouté")
    else:  # si le genre n'est pas repertorié, on l'ajoute
        print(">Genre non connu")
        # on appel la fonction qui est en charge des ajouts des genres
        genre_ajoute = nouveau_genre(biblio)
        livre = Livre(titre_livre, annee_livre, genre_ajoute)
        biblio.livre_ajout(livre)
        print("Le livre ", titre_livre, "a été ajouté")


# --- Fonctions de Suppression ---

def supprime_livre(biblio):
    """Suppression du livre selectionné"""
    titre_livre = str(input("> Entrez le titre:"))
    if biblio.supprimer_livre(titre_livre) is None: # vérification de la présence du livre
        print(titre_livre,"n'existe pas")
    biblio.supprimer_livre(titre_livre)


def supprime_genre(biblio):
    """Suppression du genre sélectionné"""
    genre = input(">Entrez le genre:")
    biblio.supprimer_genre(genre)

    # -- Fonctions de gestion des données JSON

def data(biblio):
    """Fonction qui utilise la méthode chargement_data
    pour récupérer les données du fichier JSON"""
    biblio.chargement_data()

def sauvegarde(biblio):
    """Fonction qui utilise la méthode conv_json
    pour convertir les données saisies par l'utilisateur en données JSON"""
    biblio.conv_json()
