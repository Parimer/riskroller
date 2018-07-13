"""Battle via dice."""

# imports
import random  # Requirement was random num generator, assuming pseudorandom
import argparse
from map import map

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
    """Check to ensure user selected a mode."""
    if not args.randommode and not args.inputmode:
        print('no mode selected, use -i or -r')
        exit('goodbye')


def roll_it(team):
    """Roll virtual dice as many times as size of force."""
    i = 0
    teams_rolls = []
    while i < team:
        roll = random.choice(dice)
        teams_rolls.append(int(roll))
        i = i + 1  # I prefer to be explicit with my iterators 
    return teams_rolls


def get_input():
    """Input mode, user sets invader count and defender count."""
    invaders = input('\033[92mHow many invaders (1,2, or 3)?:\033[0m ')
    defenders = input('\033[92mHow many defenders (1,2, or 3)?:\033[0m ')
    if args.verbose:
        print(f"\n\033[94mOk, The following is set:\033[0m\n\n\033[93minvaders: \033[0m{invaders}\n\033[92mdefenders: \033[0m{defenders}\n")
    return int(invaders), int(defenders)


def evaluate_rolls(invaders, defenders):
    invaders.sort(reverse=True)
    defenders.sort(reverse=True)
    invaderwins = [item1 for item1, item2 in zip(invaders, defenders) if item1 > item2]
    defenderwins = [item1 for item1, item2 in zip(defenders, invaders) if item1 > item2]
    defenderties = [item1 for item1, item2 in zip(defenders, invaders) if item1 == item2]
    total_invader_wins = len(invaderwins)
    total_defender_wins = len(defenderwins) + len(defenderties)
    if args.verbose:
        print(f'invader win list: {invaderwins}')
        print(f'defender win list: {defenderwins}')
        print(f'defender tie list: {defenderties}')
    return total_invader_wins, total_defender_wins


def main():
    """Plays a round of risk for two teams based on criteria."""
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
    # roll dice for each and store in list
    invaders_rolls = roll_it(invaders)
    defenders_rolls = roll_it(defenders)
    if args.verbose:
        print(f'Invader rolls: {invaders_rolls}\nDefender rolls: {defenders_rolls}')
    invader_wins, defender_wins = evaluate_rolls(invaders_rolls, defenders_rolls)
    print(f'Invader wins: {invader_wins}\nDefender wins: {defender_wins}\n')
# main


if __name__ == '__main__':
    main()



