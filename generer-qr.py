# Ce fichier sert de point d'entrée au programme.
# Il définit l'interface du programme avec l'extérieur et
# opère les appels aux fonctions que vous allez implémenter
# au long de ce projet.

from PIL import Image, ImageDraw, ImageFont
import argparse

def afficher(img, marges=False, numeros=False):
    if marges or numeros:
        blanc = Image.new(
            mode="RGB",
            size=(25, 25),
            color=(255, 255, 255))
        blanc.paste(img, (2, 2))
        img = blanc.resize((500, 500), resample=Image.Resampling.BOX)
        if numeros:
            dessin = ImageDraw.Draw(img)
            police = ImageFont.load_default()
            for i in range(21):
                dessin.text((23, 45 + 20 * i), '{:02d}'.format(i), font=police, fill=(63, 63, 63))
                dessin.text((45 + 20 * i, 25), '{:02d}'.format(i), font=police, fill=(63, 63, 63))
    else:
        img = img.resize((420, 420), resample=Image.Resampling.BOX)

    img.show()

def generer_qr_code(message, etape, marges=False, numeros=False):
    img = Image.new(mode="RGB", size=(21,21), color=(127, 127, 127))

    # Première étape
    import qr
    qr.placer_modules_fixes(img)

    if (etape == 1):
        afficher(img, marges=marges, numeros=numeros)
        return

    # Deuxième étape
    import encodeur
    format_encode = encodeur.encode_format(1, 3)
    qr.placer_modules_format(img, format_encode)
    if (etape == 2):
        afficher(img, marges=marges, numeros=numeros)
        return
    
    # Troisième étape
    if (etape == 3):
        donnees = [64, 116, 39, 38, 23, 102, 242, 2, 16, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 154, 167, 72, 123, 58, 205, 160]
        qr.placer_modules_donnees(img, donnees)
        afficher(img, marges=marges, numeros=numeros)
        return

    donnees = encodeur.encode_message(message)

    import galois
    correcteur = galois.Correcteur(7, 0b100011101)
    donnees += correcteur.encode(donnees)

    qr.placer_modules_donnees(img, donnees)
    afficher(img, marges=marges, numeros=numeros)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Générateur de QR-codes.')
    
    parser.add_argument('message', type=str, nargs='?', help='Message à encoder.')
    parser.add_argument('--etape', type=int, nargs='?', help='Étape à afficher.')
    parser.add_argument('--numeros', action='store_true', help='Afficher les numéros.')
    parser.add_argument('--marges', action='store_true', help='Afficher les marges.')

    args = parser.parse_args()

    generer_qr_code(args.message, args.etape, marges=args.marges, numeros=args.numeros)
