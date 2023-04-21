from PIL import Image

img = Image.new("RGB", (54, 55), (234, 234, 234))

def change_pixel_vertical(start_pixel, end_pixel, column):
    for i in range(start_pixel-1, end_pixel):
        img.putpixel((column-1, i), (0,0,0))


def change_pixel_horizontal(start_pixel, end_pixel, row):
    for i in range(start_pixel-1, end_pixel):
        img.putpixel((i, row-1), (0,0,0))
 
def fill_square(coordinate, x, y, color):
    for ii in range(y):
        for i in range(x):
            img.putpixel((i + coordinate[0], ii + coordinate[1]), color)




change_pixel_horizontal(0, 54, 30)
change_pixel_vertical(0, 55, 24)

change_pixel_horizontal(24, 45, 53)
change_pixel_vertical(31, 55, 45)

change_pixel_horizontal(46, 54, 44)
change_pixel_horizontal(46, 54, 45)



fill_square((0,0), 23, 29, (246,229,28))

fill_square((45,30), 9, 13 ,(4,70, 156))




img.show()

img_resized = img.resize((540, 550), Image.BOX)


img_resized.show()