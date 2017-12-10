from scanner import Scanner

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
