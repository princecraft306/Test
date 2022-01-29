#/usr/bin/python3

'''Our own little animal farm.'''

import sys
import time
import random


def add_animal(farm, animal):
    farm.add(animal)
    return farm

def main(animals):
    farm = set()
    for animal in animals:
        farm = add_animal(farm, animal)
    print("We've got some animals on the farm:", ', '.join(farm) + '.')
    return

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Pass at least one animal type!')
        sys.exit(1)
        a = random.randint(10, 20)
        add_animal = time.sleep(1)
    main(sys.argv[1:])
 
