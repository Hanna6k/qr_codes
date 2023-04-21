from PIL import Image

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (234, 234, 12)
WHITE = (222, 222, 222)
GREEN = (0, 153, 0)

color_blocks = [(BLUE, BLACK),(YELLOW, WHITE), (BLACK, RED), (GREEN, YELLOW), (YELLOW, WHITE), (GREEN, BLACK), (BLACK, YELLOW), (BLUE, WHITE), (YELLOW, RED), (RED, BLACK), (BLUE, WHITE), (YELLOW, BLACK)]
position_blocks = [(0,0), (8,0), (16,0),(24,0),(0,6), (8,6), (16, 6), (24, 6), (0, 12), (8, 12), (16, 12), (24, 12)]

color_dots = [RED, BLACK, WHITE, BLACK, RED, BLACK, RED, BLUE, GREEN, BLACK, BLACK, GREEN, YELLOW, BLACK, RED, GREEN]
position_dots = [(6,1),(9,0,), (22,1), (30,0), (31, 0),(1,7),(14,6), (16,6), (17,6), (25,6),(6,13), (8, 12), (9, 12), (17, 13), (24, 12), (25, 12)]

image = Image.new("RGB", (32, 18), (127, 127, 127))

dots_color = [RED, BLACK, WHITE, ]

def fill_square(coordinate, x, y, color, img):
    for ii in range(y):
        for i in range(x):
            img.putpixel((i+coordinate[0], ii+coordinate[1]), color)

def change_pixel_horizontal(img, start_pixel, end_pixel, row):
    for i in range(start_pixel-1, end_pixel):
        img.putpixel((i, row-1), (0,0,0))
    

def box(img, color1, color2, coordinate, width, height):
    fill_square(coordinate, width, height, color1, img)
    for i in range(width):
        img.putpixel((coordinate[0]+i, coordinate[1]+1), color2)
        img.putpixel((coordinate[0]+i, coordinate[1]+3), color2)
        img.putpixel((coordinate[0]+i, coordinate[1]+5), color2)
    return img

def three_dots(img, color, coordinate):
    img.putpixel((coordinate[0], coordinate[1]), color)
    img.putpixel((coordinate[0], coordinate[1] + 2), color)
    img.putpixel((coordinate[0], coordinate[1] + 4), color)


for i in range(12):

    box(image, color_blocks[i][0], color_blocks[i][1], position_blocks[i], 8, 6)

for i in range(16):
    three_dots(image, color_dots[i], position_dots[i])


image_resize = image.resize((960, 540), Image.BOX)

image_resize.show()

x = 1 << 1000
print(x)