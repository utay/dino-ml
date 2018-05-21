from generation import Generation

def main():
    generation = Generation()
    while True:
        generation.execute()
        generation.keep_best_genomes()
        generation.mutations()

if __name__ == '__main__':
    main()
