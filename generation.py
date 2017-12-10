from scanner import Scanner
from network import Network
from time import sleep
import numpy as np
import pykeyboard

class Generation:
    def __init__(self):
        self.__genomes = [Network() for i in range(12)]
        self.__best_genomes = []

    def execute(self):
        k = pykeyboard.PyKeyboard()
        scanner = Scanner()
        scanner.find_game()
        for genome in self.__genomes:
            scanner.reset()
            k.press_keys(['Command', 'r'])
            k.release_key('Command')
            sleep(1)
            k.press_key(k.space)
            while True:
                try:
                    obs = scanner.find_next_obstacle()
                    inputs = [obs['distance'], obs['length'], obs['speed']]
                    outputs = genome.forward(np.array(inputs, dtype=float))
                    if outputs[0] > 0.55:
                        k.press_key(k.space)
                except:
                    break
            genome.fitness = scanner.get_fitness()

    def keep_best_genomes(self):
        self.__genomes.sort(key=lambda x: x.fitness, reverse=True)[:4]
        self.__best_genomes = self.__genomes[:]

    def cross_over(self):
        print('cross over')

    def mutate(self):
        print('mutate')
