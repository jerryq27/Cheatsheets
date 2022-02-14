import random


class Creature:

    def __init__(self, creature_name, lvl):
        """
        Constructor method.
        Class fields are defined here, it is discourage to do this outside the __init__ function.
        :param creature_name:
        :param lvl:
        """
        self.name = creature_name
        self.level = lvl

    def __repr__(self):
        """
        "toString" function.
        :return: String representation of the object.
        """
        return "Level {} {} creature.".format(self.level, self.name)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):  # Inheriting from the Creature class.

    def __init__(self, wizard_name, lvl):
        """
        Constructor method.
        Class fields are defined here, it is discourage to do this outside the __init__ function.
        :param wizard_name:
        :param lvl:
        """
        super().__init__(wizard_name, lvl)

    def attack(self, creature):
        print("The wizard {} attacks the {}!".format(self.name, creature.name))

        # Using the D&D concept of a 12-sided die and levels to determine who wins.

        # my_roll = random.randint(1, 12) * self.level
        # creature_roll = random.randint(1, 12) * creature.level

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print("{} rolls a(n) {} and {} rolls a(n) {}.".format(self.name, my_roll, creature.name, creature_roll))
        if my_roll >= creature_roll:
            print("{} kills the {}!".format(self.name, creature.name))
            return True
        else:
            print("{} wins the fight!".format(creature.name))
            return False


class SmallAnimal(Creature):  # Unlike Java, you don't need to call the super constructor.

    # Override this function in the Creature class.
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2  # Small creature is easier to defeat than others, hence the nerf.


class Dragon(Creature):

    def __init__(self, dragon_name, lvl, scaliness, breaths_fire):
        super().__init__(dragon_name, lvl)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()

        # Traditional way.
        fire_modifier = None
        if self.breaths_fire:
            fire_modifier = 5
        else:
            fire_modifier = 1

        # 1 line Pythonic way: var = TRUE_VAL if TEST else FALSE_VALUE
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10  # 10% of the scaliness affects the roll.
        return base_roll * fire_modifier * scale_modifier


