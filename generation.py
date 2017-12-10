from scanner import Scanner
import network
import pykeyboard

class Generation:
    def __init__(self):
        self.genomes = [Network() for i in range(12)]

    def execute():
        k = pykeyboard.PyKeyboard()
        for genome in self.genomes:
            scanner = Scanner()
            scanner.find_game()
            while True:
                obstacle = scanner.find_next_obstacle()
                if obstacle:
                    output = genome.forward(np.array(obstacle, dtype=float))
                    if output > 0.55:
                        k.press_key(k.space)
            # Set genome.fitness
            # Reload game
