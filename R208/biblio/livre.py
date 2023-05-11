"""chemin pour l'environement python3"""
#!/usr/bin/env python3

class Livre:
    """
    Représente un livre dans la bibliothèque
    """

    def __init__(self, titre, annee, genre):
        """Initialisation de l'objet livre"""
        self.titre = titre
        self.annee = annee
        self.genre = genre

    def __str__(self):
        """Formatage de l'affichage des livres"""
        if self.genre == "":
            return f"{self.annee},  {self.titre}" # affichage du livre sans genre
        return f"{self.annee}, [{self.genre}],  {self.titre}" # affichage du livre

    def __lt__(self, other):
        """Méthode de comparaison et de tri des livres"""
        if self.annee != other.annee:
            return self.annee < other.annee
        if self.genre != other.genre:
            return self.genre < other.genre
        return self.titre < other.titre
