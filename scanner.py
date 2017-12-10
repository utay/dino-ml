from PIL import Image
import pykeyboard
import os

dino_color = (83, 83, 83, 255)

def screenshot(x, y, w, h):
    os.system("screencapture -R{},{},{},{} tmp.png".format(x, y, w, h))
    img = Image.open("tmp.png")
    return img

def is_dino_color(pixel):
    return pixel == dino_color

class Scanner:
    def __init__(self):
        self.dino_start = (0, 0)
        self.dino_end = (0, 0)

    def find_game(self):
        image = screenshot(0, 0, 1500, 1500)
        size = image.size
        pixels = []
        for y in range(0, size[1], 10):
            for x in range(0, size[0], 10):
                color = image.getpixel((x, y))
                if is_dino_color(color):
                    pixels.append((x, y))

        if not pixels:
            raise Exception("Game not found!")

        self.__find_dino(pixels)

    def __find_dino(self, pixels):
        start = pixels[0]
        end = pixels[1]
        for pixel in pixels:
            if pixel[0] < start[0] and pixel[1] > start[1]:
                start = pixel
            if pixel[0] > end[0] and pixel[1] > end[1]:
                end = pixel
        self.dino_start = start
        self.dino_end = end

    def find_next_obstacle(self, image):
        for x in range(0, 1000, 5):
            for y in range(0, 310, 5):
                color = image.getpixel((x, y))
                if is_dino_color(color):
                    print(x, y)
                    return x
        return 0

scanner = Scanner()
scanner.find_game()
k = pykeyboard.PyKeyboard()
print(scanner.dino_end)
while True:
    x = scanner.dino_end[0]
    y = scanner.dino_end[1]
    image = screenshot(200, 100, 500, 155)
    x = scanner.find_next_obstacle(image)
    if x > 0 and x < 80:
        k.press_key(k.space)
