# Ce fichier contient des classes de tests
# pour les différentes étapes du projet.

from PIL import Image

import unittest

class Etape1(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(Etape1, self).__init__(*args, **kwargs)
        self.reference = Image.open("tests/etape1.png")
        self.img = Image.new(mode="RGB", size=(21,21), color=(127, 127, 127))
        import qr
        qr.placer_modules_fixes(self.img)

    def __del__(self):
        self.reference.close()

    def test_dimensions(self):
        self.assertEqual(self.img.size, (21, 21))
    
    def test_modules(self):
        for x in range(21):
            for y in range(21):
                self.assertEqual(self.img.getpixel((x, y)), self.reference.getpixel((x, y)), 
                    "La couleur n'est pas celle attendue aux coordonnées ({}, {})".format(x, y))


class Etape2(unittest.TestCase):

    def test_placement_modules(self):
        img = Image.new(mode="RGB", size=(21,21), color=(127, 127, 127))
        import qr
        qr.placer_modules_fixes(img)
        qr.placer_modules_format(img, 30877)
        reference = Image.open("tests/etape2.png")

        for x in range(21):
            for y in range(21):
                self.assertEqual(img.getpixel((x, y)), reference.getpixel((x, y)), 
                    "La couleur n'est pas celle attendue aux coordonnées ({}, {})".format(x, y))

    def test_modulo(self):
        in_outs = [
            ((7, 8), 7),
            ((5, 7), 2),
            ((17, 12), 5),
            ((14, 1), 0),
            ((17, 11), 7),
        ]

        import galois

        for ((a, b), r) in in_outs:
            self.assertEqual(galois.modulo(a, b), r,
                "Le modulo n'est pas le bon pour les paramètres {:b} ({}) et {:b} ({}), "
                "le résultat attendu est {:b} alors que le résultat obtenu "
                "est {:b}".format(a, a, b, b, r, galois.modulo(a, b)))

    def test_encodage_format(self):
        in_outs = [
            ((1, 3), 30877),
            ((0, 0), 21522),
            ((2, 0), 5769),
            ((2, 5), 597),
            ((3, 7), 11245),
        ]
        import encodeur

        for ((l, m), r) in in_outs:
            self.assertEqual(encodeur.encode_format(l, m), r,
                "L'encodage du format n'est pas le bon pour les paramètres {} et {}, "
                "le résultat attendu est {:015b} alors que le résultat obtenu est {:015b}".format(l, m, r, encodeur.encode_format(l, m)))

class Etape3(unittest.TestCase):

    def test_placement_modules(self):
        img = Image.new(mode="RGB", size=(21,21), color=(127, 127, 127))
        import qr
        qr.placer_modules_fixes(img)
        qr.placer_modules_format(img, 30877)
        message = [64, 116, 39, 38, 23, 102, 242, 2, 16, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 154, 167, 72, 123, 58, 205, 160]
        qr.placer_modules_donnees(img, message)
        reference = Image.open("tests/etape3.png")

        for x in range(21):
            for y in range(21):
                self.assertEqual(img.getpixel((x, y)), reference.getpixel((x, y)), 
                    "La couleur n'est pas celle attendue aux coordonnées ({}, {})".format(x, y))

    def test_encodage_format(self):
        in_outs = [
            ("Bravo !", [64, 116, 39, 38, 23, 102, 242, 2, 16, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17]),
            ("", [64, 0, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 236]),
            ("Un test plus long", [65, 21, 86, 226, 7, 70, 87, 55, 66, 7, 6, 199, 87, 50, 6, 198, 246, 230, 112])
        ]
        import encodeur

        for (s, r) in in_outs:
            self.assertEqual(encodeur.encode_message(s), r,
                "L'encodage du message {} n'est pas le bon".format(str(s)))

class Etape4(unittest.TestCase):
    
    def test_corps_addition(self):
        in_outs = [
            ((1, 2), 3),
            ((1, 1), 0),
            ((19, 19), 0),
            ((10, 12), 6),
        ]

        import galois
        corps = galois.CorpsGalois(285)

        for (a, b), r in in_outs:
            self.assertEqual(corps.plus(a, b), r,
                "L'addition des polynomes {:08b} et {:08b} "
                "ne donne pas le résultat attendu".format(a, b))

    def test_corps_multiplication(self):
        in_outs = [
            ((1, 2), 2),
            ((1, 1), 1),
            ((19, 19), 24),
            ((10, 12), 120),
            ((220, 134), 192),
            ((134, 220), 192),
            ((255, 255), 226),
            ((0, 14), 0),
            ((14, 0), 0),
        ]

        import galois
        corps = galois.CorpsGalois(285)

        for (a, b), r in in_outs:
            self.assertEqual(corps.fois(a, b), r,
                "L'addition des polynomes {:08b} et {:08b} "
                "ne donne pas le résultat attendu".format(a, b))

    def test_corps_division(self):
        in_outs = [
            ((1, 1), 1),
            ((19, 19), 1),
            ((120, 12), 10),
            ((1, 2), 142),
            ((192, 220), 134),
            ((192, 134), 220),
            ((0, 14), 0),
        ]

        import galois
        corps = galois.CorpsGalois(285)

        for (a, b), r in in_outs:
            self.assertEqual(corps.division(a, b), r,
                "La division du polynome {:08b} par le polynome {:08b} "
                "ne donne pas le résultat attendu".format(a, b))

    def test_corps_puissance(self):
        in_outs = [
            ((1, 1), 1),
            ((19, 0), 1),
            ((167, 1), 167),
            ((1, 14), 1),
            ((2, 2), 4),
            ((3, 3), 15),
            ((2, 4), 16),
            ((2, 5), 32),
            ((2, 7), 128),
            ((2, 8), 29),
            ((2, 9), 58),
            ((2, 12), 205),
            ((255, 100), 230)
        ]

        import galois
        corps = galois.CorpsGalois(285)

        for (a, b), r in in_outs:
            self.assertEqual(corps.puissance(a, b), r,
                "La puissance {} du polynome {:08b} "
                "ne donne pas le résultat attendu".format(b, a))
        

class Etape5(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()