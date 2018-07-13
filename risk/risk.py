"""Battle via dice."""

# imports
import random  # Requirement was random num generator, assuming pseudorandom
import argparse
from map import map
from pprint import pprint

# globals
dice = [1, 2, 3, 4, 5, 6]
forces = [1, 2, 3]

# arguments
parser = argparse.ArgumentParser(description='game of chance', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-r', '--randommode', help='randommode', action='store_true')
parser.add_argument('-n', '--no-logo', dest='logo_off', help='disables printing logo', action='store_true', default=False)
parser.add_argument('-t', '--test', help='prints out james campbell data', action='store_true', default=False)
parser.add_argument('-v', '--verbose', help='print more stuff', action='store_true')
parser.add_argument('-i', '--inputmode', action='store_true')
args = parser.parse_args()

# functions

def random_outcome(invading_forces, defending_forces):
    i = 0
    while i < invading_forces:
        roll = random.choice(dice)  # choice always faster than shuffle, had to confirm
        print(roll)
        i = i + 1
        exit()

def check_mode():
    if not args.randommode and not args.inputmode:
        print('no mode selected, use -i or -r')
        exit('goodbye')

def main():
    if not args.logo_off:
        print(map)
    # make sure the user set a mode or ask them to and run again
    check_mode()
    # based on the mode, get the invaders count and defenders count
    if args.inputmode:
        invaders, defenders = get_input()
    else:
        if args.randommode:
            invaders = random.choice(forces)
            defenders = random.choice(forces)


# main

if __name__ == '__main__':
    main()



