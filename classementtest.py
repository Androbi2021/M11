import unittest
import random
from classement_ordered import Classement
from coureur    import Coureur
from temps      import Temps
from resultat   import Resultat

coureurs = [ Coureur("Alixe", 24), \
            Coureur("Amos", 27), \
            Coureur("Robin", 19), \
            Coureur("Daniel", 31),  \
            Coureur("Emma", 25),  \
            Coureur("Fred", 28),  \
            Coureur("Gerard", 25) ]

class ClassementTest(unittest.TestCase):
    def setUp(self):
        self.c1 = coureurs[0]
        self.c2 = coureurs[1]
        self.c3 = coureurs[2]

        t = Temps(1,2,3)
        t2 = Temps(0,5,6)
        self.r1 = Resultat(self.c1, t)
        self.r2 = Resultat(self.c2, t2)

        self.r3 = Resultat(self.c3, t)

        self.cl = Classement()
        self.cl.add(self.r1)
        self.cl.add(self.r2)
    
    def test_init(self):
        self.assertNotEqual(self.cl.get_position(self.c1), -1, "Le premier coureur ne s'est pas ajouté dans la liste")
        self.assertNotEqual(self.cl.get_position(self.c2), -1, "Le deuxième coureur ne s'est pas ajouté dans la liste")

    def test_size(self):
        self.assertEqual(self.cl.size(), 2, "La méthode size de classement ne retourne pas la bonne taille")

    def test_add(self):
        self.cl.add(self.r3)
        self.assertEqual(self.cl.size(), 3, "La méthode add de classement n'ajoute pas correctement un coureur")

    def test_get(self):
        self.assertEqual(self.cl.get(self.c1), self.r1, "La méthode get de classement ne retourne pas le bon résultat")

    def test_get_position(self):
        self.assertEqual(self.cl.get_position(self.c2), 1, "La méthode get_position de classement ne retourne pas la bonne position")

    def test_remove(self):
        self.cl.remove(self.c1)
        self.assertEqual(self.cl.size(), 1, "La méthode remove de classement ne retire pas correctement le coureur")

if __name__ == '__main__':
    unittest.main(verbosity=2)