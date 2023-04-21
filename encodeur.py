# Dans ce fichier, nous implémenterons les diverses fonctions d'encodage.

from galois import *

def encode_message(message):
    bits = 0b0100  # Le mode d'encodage, sur 4 bits.


    octets_message = message.encode('iso-8859-1')
    longueur = len(octets_message)
    if longueur > 17:
        raise ValueError('Le message est trop long')

    # Ajouter la longueur du message, sur 8 bits.
    bits <<= 8
    bits = bits ^ longueur

    # Ajouter les octets du message.
    #bits << 8* len(message)
    #bits = bits^octets_message

    for i in octets_message:
        bits <<= 8
        bits = bits ^ i

    bits <<= 4

    # Ajouter les octets de "rembourrage".
    for i in range (17 - longueur):
        bits <<= 8
        if i % 2 == 0:
            bits = bits^236
        else:
            bits = bits^17

    # Regroupement des bits en octets.
    octets = []
    for i in range(19):
        octets.insert(0, bits & 255)
        bits >>= 8
    
    return octets


