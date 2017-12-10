from scanner import Scanner
import pykeyboard

def main():
    scanner = Scanner()
    scanner.find_game()
    k = pykeyboard.PyKeyboard()
    print(scanner.dino_end)
    while True:
        obstacle = scanner.find_next_obstacle()
        if obstacle:
            k.press_key(k.space)

if __name__ == '__main__':
    main()
