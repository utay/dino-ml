from PIL import ImageGrab
import pykeyboard


dino_color = (83, 83, 83, 255)

dino_start = (0, 0)
dino_end = (0, 0)

def is_dino_color(pixel):
    return pixel == dino_color

def find_dino(pixels):
    start = pixels[0]
    end = pixels[1]
    for pixel in pixels:
        if pixel[0] < start[0] and pixel[1] > start[1]:
            start = pixel
        if pixel[0] > end[0] and pixel[1] > end[1]:
            end = pixel
    return start, end

def find_game():
    image = ImageGrab.grab()
    size = image.size
    pixels = []
    for y in range(0, size[1], 10):
        for x in range(0, size[0], 10):
            color = image.getpixel((x, y))
            if is_dino_color(color):
                pixels.append((x, y))

    if not pixels:
        raise Exception("Game not found!")

    return find_dino(pixels)

def find_next_obstacle(image):
    for x in range(0, 600, 5):
        for y in range(0, 170, 5):
            if is_dino_color(image.getpixel((x, y))):
                return x
    return 0

dino_start, dino_end = find_game()
k = pykeyboard.PyKeyboard()
print(dino_end)
while True:
    x1 = dino_end[0] + 80
    y1 = dino_end[1] - 150
    x2 = x1 + 600
    y2 = y1 + 170
    image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    x = find_next_obstacle(image)
    if x:
        k.press_key(k.space)
