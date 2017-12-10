from PIL import Image
from datetime import datetime
import os

dino_color = (83, 83, 83, 255)

def screenshot(x, y, w, h):
    os.system("screencapture -R{},{},{},{} tmp.png".format(x, y, w, h))
    img = Image.open("tmp.png")
    return img

def is_dino_color(pixel):
    return pixel == dino_color

class Obstacle:
    def __init__(self, distance, length, speed):
        self.distance = distance
        self.length = length
        self.speed = speed

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

    def find_next_obstacle(self):
        dist0, t0 = self.__next_obstacle()
        dist1, t1 = self.__next_obstacle()
        dist = dist0 - dist1
        speed = dist / ((t1 - t0).microseconds * 1000)
        return Obstacle(dist1, 0, speed) if dist > 0 else None

    def __next_obstacle(self):
        image = screenshot(200, 100, 500, 155)
        dist = self.__next_obstacle_dist(image)
        return dist, datetime.now()

    def __next_obstacle_dist(self, image):
        for x in range(0, 1000, 5):
            for y in range(0, 310, 5):
                color = image.getpixel((x, y))
                if is_dino_color(color):
                    return x
        return 0
