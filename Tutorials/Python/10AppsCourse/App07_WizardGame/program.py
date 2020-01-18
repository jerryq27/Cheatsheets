import random
import time

from App07_WizardGame.gobjects import Wizard, Creature, SmallAnimal, Dragon
from Common import app


def game_loop():
    creatures = [
        SmallAnimal("Toad", 1),
        Creature("Tiger", 12),
        SmallAnimal("Bat", 3),
        Dragon("Dragon", 50, 75, True),
        Wizard("Evil Wizard", 1000)
    ]
    hero = Wizard("Gandolf", 75)

    in_game = True
    while in_game:
        active_creature = random.choice(creatures)  # random.choice() selects a random item from a collection.
        print("A {} of level {} has appeared from the dark and foggy forest...\n".format(active_creature.name,
                                                                                         active_creature.level))

        user_input = input("Do you [a]ttack, [r]unaway, or [l]ook around? ").lower().strip()
        if user_input == "a":
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("{} was defeated and needs to rest...".format(hero.name))
                time.sleep(5)
                print("{} has recovered!".format(hero.name))
        elif user_input == "r":
            print("The hero {} has become unsure of his power and flees!".format(hero.name))
        elif user_input == "l":
            print("The hero {} looks around to see...".format(hero.name))
            for creature in creatures:
                print(" * A {} of level {}.".format(creature.name, creature.level))
        else:
            print("Exiting game..")
            in_game = False

        if not creatures:  # The creatures list returns False if it is empty.
            print("Congratulation! You've defeated all the creatures! You win!")
            in_game = False


if __name__ == '__main__':
    app.print_title("Wizard Game app")
    game_loop()
