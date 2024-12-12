from ordered_linked_list import OrderedLinkedList

class Classement :

    def __init__(self):
        """
        @pre: -
        @post: un classement vide de taille 0 a été créé
        """
        self.__resultats = OrderedLinkedList()  # Liste chaînée pour stocker les résultats
        self.__size = 0                         # Nombre de résultats actuels (initialement 0)


    def size(self):
        """
        Méthode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de résultats actuellement stockés dans ce classement a été retourné.
        """
        return self.__size

    def add(self, r):
        """
        Ajoute un résultat r dans ce classement.
        @pre: r est une instance de la classe Resultat
        @post: Le résultat r a été inséré selon l'ordre du classement.
            En cas d'ex-aequo, r est inséré après les autres résultats de même ordre.
        """
        self.__size += 1
        self.__resultats.add_middle(r)  # Ajout dans la liste chaînée tout en maintenant l'ordre


    def get(self,c):
        """
        Retourne le résultat d'un coureur donné.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        current = self.__resultats.first()
        while current is not None:
            if current.value().coureur() == c:
                return current.value()
            current = current.next()
        return None  # Coureur non trouvé

    def get_position(self, c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post retourne un entier représentant la position du coureur c dans ce classement,
            à partir de 1 pour la tête de ce classement.
            Retourne -1 si le coureur ne figure pas dans le classement.
        """
        current = self.__resultats.first()
        position = 1
        while current is not None:
            if current.value().coureur() == c:
                return position
            current = current.next()
            position += 1
        return -1  # Coureur non trouvé

    def remove(self, c):
        """
        Retire un résultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) résultat pour le coureur c du classement.
            Retourne c si un résultat a été retiré, ou False si c n'est pas trouvé.
        """
        current = self.__resultats.first()
        while current is not None:
            if current.value().coureur() == c:
                self.__resultats.remove_middle(current.value())  # Supprime le Node correspondant
                self.__size -= 1
                return c
            current = current.next()
        return False  # Coureur non trouvé


    def __str__(self):
        """
        Méthode magique
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: Retourne une représentation de ce classement sous forme d'un string,
               avec une ligne par résultat.
        """
        s = ""
        d = self.__resultats
        current = d.first()
        while current is not None:
            c = current.value().coureur()
            t = current.value().temps()
            s += "  " + str(self.get_position(c)) + " > " + str(t) + " " + str(c) + "\n"
            current = current.next()
        return s