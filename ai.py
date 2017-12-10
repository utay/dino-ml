from generation import Generation

def main():
    # Execute one Generation
    generation = Generation()
    generation.execute()
    # Remove the worst genomes until we have 4
    # Cross over and random mutations until we got 12 genomes again

if __name__ == '__main__':
    main()
