"""Importation des bibliothèques json, os et livre"""
import json
import os
from biblio.livre import Livre

#!/usr/bin/env python3

class Bibliotheque:
    """Reprsénte un bibliothèque 
    avec une liste de livres et de genres """
    def __init__(self):
        """Initialisation de l'objet bibliothèque"""
        self.livre = []
        self.genre = []

    def chargement_data(self):
        """Chargement des données venant du fichier json"""
        #Cette variable contient l'emplacement du fichier du fichier JSON
        filename = os.path.expanduser("~/biblio.json")
        try:
            with open(filename, "r", encoding="utf-8") as filedesc:  # ouverture du fichier json
                donnees = json.load(filedesc)  # chargement des données json
                print("Chargement des données")
            # ajout des données  dans les objets de la bibliothèque
                for i in donnees["genre"]:
                    self.genre.append(i)  # ajout dans la liste genre
                for i in donnees["livre"]:
                    self.livre.append(
                    # ajout les objets livres dans la liste des livres
                    Livre(i["titre"], i["annee"], i["genre"]))
            # Si le fichier n'existe pas , on initialise un bibliothèque vide
        except FileNotFoundError:
            print("Fichier de sauvegarde introuvable")
            print("Initialisation avec une bibliothèque vide.")
            self.genre = []
            self.livre = []
            # si le fichier json est mal formé, on initialise la bibliothèque vide
        except json.JSONDecodeError:
            print("Fichier de sauvegarde mal formé")
            print("Initialisation avec une bibliothèque vide.")
            self.genre = []
            self.livre = []
            # s'il y a un problème pour sauvegarder le fichier json.
        except IOError:
            print("Impossible d'écrire dans le fichier de sauvegarde")
            print("La bibliothèque ne sera pas sauvegardée.")

    def genre_ajout(self, genre):
        """Méthode d'ajout de genre dans la liste de la bibliothèque"""
        self.genre.append(genre)
        print("Nous avons ajouté ce genre")

    def genre_existe(self, genre):
        """Méthode qui renvoie un booléen si le genre existe ou non"""
        return genre in self.genre

    def livre_ajout(self, livre):
        """Méthode qui ajoute un livre dans la liste"""
        self.livre.append(livre)

    def afficher_livre(self):
        """
        Méthode qui permet d'afficher la liste des livres
        """
        print("Nous avons trouvé", len(self.livre), "livre(s)")
        # La fonction sorted permet de trier la liste des livres
        # selon la méthode __lt__ de la classe Livre
        trie = sorted(self.livre)
        for livre in trie:
            # Affichage des livres selon le format du __str__ de la classe Livre
            print(livre)


    def afficher_genre(self):
        """
        Méthode qui permet d'afficher les genres
        """
        # Initialisation d'un dictionnaire
        # pour stocker les genres et leur nombre de livres correspondant
        genres = {}
        # Si les deux listes sont vides
        if not self.livre and not self.genre:
            print("Aucun genre enregistré")
        # Si la bibliothèque est vide, afficher "Aucun livre" pour chaque genre
        elif not self.livre:
            for i in self.genre:
                print(i, ": Aucun livre")
        # Sinon, parcourir tous les livres pour compter le nombre de livres par genre
        else:
            for livre in self.livre:
                # Si le genre existe déjà dans le dictionnaire, ajouter 1 au nombre de livres
                if livre.genre in genres:
                    genres[livre.genre] += 1
                else:  # Sinon, initialiser le nombre de livres à 1
                    genres[livre.genre] = 1

            # Afficher le nombre de livres pour chaque genre dans l'ordre alphabétique
            for genre, nb_livres in sorted(genres.items()):
                if genre == "":
                    genre = "sans genre"  # Si le genre est vide, remplacer par "sans genre"
                print(genre, ":", nb_livres, "livre(s)")

            # Afficher "Aucun livre" pour les genres qui n'ont pas de livre associé
            for genre in self.genre:
                if genre not in genres:
                    print(genre, ": Aucun livre")


    def supprimer_livre(self, titre):
        """
        Méthode qui permet de supprimer un livre
        """
        for livre in self.livre:
            if titre == livre.titre:
                self.livre.remove(livre)  # Le livre correspond à la cible
                print(">Suppression du livre", livre.titre)
                return livre
        return None

    def supprimer_genre(self, selec_genre):
        """
        Méthode qui permet de supprimer le genre"""
        if selec_genre in self.genre:
            self.genre.remove(selec_genre)  # Suppression du genre
            print(">Supression du genre")
        else:
            print(">Ce genre n'existe pas ")
        for livre in self.livre:
            # Si le genre supprimé est associé à un livre, on remplace la valeur par ""
            if livre.genre == selec_genre:
                livre.genre = ""

    def conv_json(self):
        """Méthode qui convertit les données de la bibliothèque
        en un dictionnaire et qui l'ajoute au fichier json"""
        # Création du dictionnaire data
        data = {
            # initialisation de la liste des livres
            "livre": [],
            # la clé genre du dictionnaire pprends en valeur la variable self.genre
            "genre": self.genre
        }
        for livre in self.livre:
            # ajout dans la clé livre, les valeurs titre,année et genre de chaque livre
            data["livre"].append({
                "titre": livre.titre,
                "annee": livre.annee,
                "genre": livre.genre
            })
        filename = os.path.expanduser("~/biblio.json")
        # Ouverture du fichier json en mode écriture
        with open(filename, "w", encoding="utf-8") as filecontent:
            # Ajout des informations du dictionnaire data dans le fichier json
            json.dump(data, filecontent, indent=4)
        return data
    