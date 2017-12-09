from PIL import ImageGrab

image = ImageGrab.grab()
size = image.size

dinau_color = (83, 83, 83, 255)

def is_dinau_color(pixel):
    return pixel == dinau_color

def find_left_bottom_point(pixels):
    min_pixel = pixels[0]
    for pixel in pixels:
        if pixel[0] < min_pixel[0] and pixel[1] > min_pixel[1]:
            min_pixel = pixel
    return min_pixel

def find_game():
    pixels = []
    for y in range(0, size[1], 10):
        for x in range(0, size[0], 10):
            color = image.getpixel((x, y))
            if is_dinau_color(color):
                pixels.append((x, y))

    if not pixels:
        raise Exception("Game not found!")

    min_pixel = find_left_bottom_point(pixels)

    print(min_pixel)


find_game()

for x in range(10, 0, -1):
    print(x)
