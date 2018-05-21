from PIL import Image
from PIL import ImageGrab
from datetime import datetime
import os

dino_color = (83, 83, 83)

def screenshot(x, y, w, h):
    # os.system("screencapture -R{},{},{},{} tmp.png".format(x, y, w, h))
    img = ImageGrab.grab()
    img.save("tmp.png")
    save = Image.open("tmp.png")
    return save

def is_dino_color(pixel):
    return pixel == dino_color

def obstacle(distance, length, speed, time):
    return { 'distance': distance, 'length': length, 'speed': speed, 'time': time }

class Scanner:
    def __init__(self):
        self.dino_start = (0, 0)
        self.dino_end = (0, 0)
        self.last_obstacle = {}
        self.__current_fitness = 0
        self.__change_fitness = False

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
        print("Game found!")
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
        image = screenshot(210, 100, 500, 155)
        dist = self.__next_obstacle_dist(image)
        if dist < 50 and not self.__change_fitness:
            self.__current_fitness += 1
            self.__change_fitness = True
        elif dist > 50:
            self.__change_fitness = False
        time = datetime.now()
        delta_dist = 0
        speed = 0
        if self.last_obstacle:
            delta_dist = self.last_obstacle['distance'] - dist
            speed = (delta_dist / ((time - self.last_obstacle['time']).microseconds)) * 10000
        self.last_obstacle = obstacle(dist, 1, speed, time)
        return self.last_obstacle

    def __next_obstacle_dist(self, image):
        s = 0
        for y in range(0, 250, 5):
            for x in range(0, 1000, 5):
                color = image.getpixel((x, y))
                if is_dino_color(color):
                    s += 1
        if s > 150:
            raise Exception('Game over!')

        for x in range(0, 1000, 5):
            for y in range(0, 310, 5):
                color = image.getpixel((x, y))
                if is_dino_color(color):
                    return x
        return 1000000

    def reset(self):
        self.last_obstacle = {}
        self.__current_fitness = 0
        self.__change_fitness = False

    def get_fitness(self):
        return self.__current_fitness
