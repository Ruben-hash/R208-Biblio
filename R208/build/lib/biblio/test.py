#!/usr/bin/env python3

from biblio.bibliotheque import Bibliotheque
from biblio import commandes


def main():
    """
    Fonction principale du programme:
    Elle appelle les commandes correspondantes à la saisie utilisateur
    """
    rep = ""
    biblio = Bibliotheque()
    commandes.data(biblio)

    while rep != "Q":
        rep = input(">Entrez votre commande (M pour afficher le menu ) :").upper()
        if rep == "M":
            commandes.afficher_menu()
        elif rep == "LG":
            print("---Affichage de la liste des genres---")
            commandes.affiche_genre(biblio)
        elif rep == "LL":
            print("---Affichage de la liste des livres---")
            commandes.affiche_livre(biblio)
        elif rep == "NG":
            print("---Ajout d'un nouveau genre---")
            commandes.nouveau_genre(biblio)
        elif rep == "NL":
            print("---Ajout d'un nouveau livre---")
            commandes.nouveau_livre(biblio)
        elif rep == "SG":
            print("---Supprimer un genre de la base de données---")
            commandes.supprime_genre(biblio)
        elif rep == "SL":
            print("---Supprimer un livre de la bibliothèque---")
            commandes.supprime_livre(biblio)
        else:
            print("---Sauvegarde des données---")
            commandes.sauvegarde(biblio)

main()
