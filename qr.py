# Ce fichier contiendra les fonctions de
# placement de modules du QR-code généré.

from PIL import Image
from galois import *
from encodeur import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)

# image = Image.new("RGB", (21, 21), GRAY)

def fill_square(img, coordinate, length, height,color):
    for ii in range(height):
        for i in range(length):
            img.putpixel((i + coordinate[0], ii + coordinate[1]), color)

def placer_module(img, x, y, couleur):
    img.putpixel((x, y), couleur)


def qr_button(coordinates, img):
    fill_square(img, coordinates, 7, 7, BLACK)
    coordinates = (coordinates[0] + 1, coordinates[1] + 1)
    fill_square(img, coordinates, 5, 5, WHITE)
    coordinates = (coordinates[0] + 1, coordinates[1] + 1)
    fill_square(img, coordinates, 3, 3, BLACK)

def set_pixel_horizontal(img, coordinate, num_pixel):
    for i in range(num_pixel):
        if i % 2 == 0:
            img.putpixel((coordinate[0] + i, coordinate[1]), BLACK)
            
        else:
            img.putpixel((coordinate[0] + i, coordinate[1]), WHITE)


def set_pixel_vertical(img, coordinate, num_pixel):
    for i in range(num_pixel):
        if i % 2 == 0:
            img.putpixel((coordinate[0], coordinate[1] + i), BLACK)            
        else:
            img.putpixel((coordinate[0], coordinate[1] + i), WHITE)



def placer_modules_fixes(img):
    img.putpixel((8, 13), BLACK)

    fill_square(img,(0,0), 8, 8, WHITE)
    fill_square(img,(13,0), 8,8, WHITE)
    fill_square(img,(0, 13), 8,8, WHITE)

    qr_button((0,0), img)
    qr_button((0,14) ,img)
    qr_button((14, 0), img)

    set_pixel_horizontal(img, (8,6), 5)
    set_pixel_vertical(img, (6, 8), 5)

    return img


def bit(n, i):
    return (n >> i) & 1 #101010

def couleur_module(b):
    if b == 0:
        return WHITE
    return BLACK

def placer_modules_format(img, format_encode):
    pos1_of_format = [(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(8,7),(8,8),(7,8),(5,8),(4,8),(3,8),(2,8),(1,8),(0,8)]
    pos2_of_format = [(20,8),(19,8),(18,8),(17,8),(16,8),(15,8),(14,8),(13,8),(8,14),(8,15),(8,16),(8,17),(8,18),(8,19),(8,20)]

    for i in range(len(pos1_of_format)):
        img.putpixel((pos1_of_format[i][0], pos1_of_format[i][1]), couleur_module(bit(format_encode, i)) )       
        img.putpixel((pos2_of_format[i][0], pos2_of_format[i][1]), couleur_module(bit(format_encode, i)) )


def applique_masque(x, y, b):
    m = 1 if (x + y) % 3 == 0 else 0
    return b ^ m

def placer_module_donnee(img, x, y, b):
    placer_module(img, x, y, couleur_module(applique_masque(x, y, b)))

def placer_modules_donnees(img, octets):
    coordinates = [(19,17,0),(19,13,0),(19,9,0),(17,9,1),(17,13,1),(17,17,1),(15,17,0),(15,13,0),(15,9,0),(13,9,1),(13,13,1),(13,17,1),(11,17,0),(11,13,0),(11,9,0),(11,4,2),(11,0,0),(9,0,1),(9,4,3), (9,9,1),(9,13,1),(9,17,1),(7,9,0),(4,9,1), (2,9,0), (0,9,1)]
    count = -1
    for i in coordinates:
        count += 1
        if i[2] == 0:  
            placer_octet_montant(img, octets[count], i[0], i[1])

        if i[2] == 1:
            placer_octet_descendant(img,octets[count], i[0], i[1])

        if i[2] == 2:
            placer_octet_montant_separe(img, octets[count], i[0], i[1])

        if i[2] == 3:
            placer_octet_descendant_separe(img, octets[count], i[0], i[1])

    

def placer_octet_montant(img, octet, x, y): #red octet((), (), ())
    pos_pixel_byte = []
    count = 0
    for h in range(4):
        for l in range(2):
            x += l
            pos_pixel_byte.append((x, y, bit(octet, count)))
            
            count += 1
        y += 1
        x -= 1

    for elements in pos_pixel_byte:
        placer_module_donnee(img, elements[0], elements[1], elements[2])


def placer_octet_descendant(img, octet, x, y):  #blue
    pos_pixel_byte = []
    count = 0
    y += 3
    for i in range(4):

        for l in range(2):
            x += l
            pos_pixel_byte.append((x, y, bit(octet, count)))
            count += 1
        y -= 1
        x -= 1
    
    for elements in pos_pixel_byte:
        placer_module_donnee(img, elements[0], elements[1], elements[2]) 



def placer_octet_montant_separe(img, octet, x, y):
    pos_pixel_byte = []
    count = 0
    y_not_fill = y + 2
    for i in range(4):
        if y == y_not_fill:
            y += 1
    
        for i in range(2):
            x += i
            pos_pixel_byte.append((x, y, bit(octet, count)))
            count += 1
        y += 1
        x -= 1
    
    for elements in pos_pixel_byte:
        placer_module_donnee(img, elements[0], elements[1], elements[2]) 



def placer_octet_descendant_separe(img, octet, x, y):
    pos_pixel_byte = []
    count = 0
    y_not_fill = y +2
    y += 4
    for i in range(4):
        if y == y_not_fill:
            y -= 1

        for l in range(2):
            x += l
            pos_pixel_byte.append((x, y, bit(octet, count)))
            count += 1
        y -= 1
        x -= 1

    for elements in pos_pixel_byte:
        placer_module_donnee(img, elements[0], elements[1], elements[2]) 



oct = [64, 116, 39, 38, 23, 102, 242, 2, 16, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 154, 167, 72, 123, 58, 205, 160]
fine =[64, 100, 102, 150, 230, 82, 2, 16, 236, 17, 236, 17, 236, 17, 236, 17, 236, 17, 236, 154, 167, 72, 123, 58, 205, 160]

# placer_modules_fixes(image)

# placer_modules_format(image, encode_format(1,3))

# placer_modules_donnees(image, fine)



# image = image.resize((630, 630), Image.BOX)

# image.show()
