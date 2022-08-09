import random

dndraces = ["dwarf", "elf", "halfling", "human", "dragonborn", "gnome", "half-elf", "half-orc", "tiefling"]

dndsubraces = {"dwarf": ["hill", "mountain"], "elf": ["high", "wood", "dark"], "halfling": ["lightfoot", "stout"], "human": ["standard", "variant"], "dragonborn": "", "gnome": ["forest", "rock"], "half-elf": "", "half-orc": "", "tiefling": ""}

dndsubracecount = {key: len(value) for key, value in dndsubraces.items()}
#Note that this gives "dwarf" a count of 2, but "tiefling" a count of 0, not 1

dndclasses = ["barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer", "warlock", "wizard"] #12 total classes

dndsubclasses = {"barbarian": ["Path of the Berserker", "Path of the Totem Warrior"], "bard": ["College of Lore", "College of Valor"], "cleric": ["Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Tempest Domain", "Trickery Domain", "War Domain"], "druid": ["Circle of the Land", "Circle of the Moon"], "fighter": ["Champion", "Battle Master", "Eldritch Knight"], "monk": ["Way of the Open Hand", "Way of Shadow", "Way of the Four Elements"], "paladin": ["Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance"], "ranger": ["Hunter", "Beast Master"], "rogue": ["Thief", "Assassin", "Arcane Trickster"], "sorcerer": ["Draconic Bloodline", "Wild Magic"], "warlock": ["Archfey", "Fiend", "Great Old One"], "wizard": ["Abjuration", "Conjuration", "Divination", "Enchantment", "Evocation", "Illusion", "Necromancy", "Transmutation"]}

dndsubclasscount = {key: len(value) for key, value in dndsubclasses.items()} 
#2 barbarians, bards, druids, rangers, sorcerers
#3 fighters, monks, paladins, rogues, warlocks
#7 clerics and 8 wizards

def character_builder():
    my_race = ""
    my_subrace = ""
    my_class = ""
    my_subclass = ""
    
    print("Hello! Welcome to the D&D random character generator. To create your character, we will be asking you to roll various dice and enter the results. \nAt any point, if you would rather we roll for you, simply type '0' instead! ")

# dndsubraces[my_race] will give list of subraces for given race
# dndsubracecount[my_race] will give integer of how many subraces a race has
    
    race_roll = int(input("First, let's determine your character's race. Roll a d10 and enter the number: "))
    while race_roll >= 10:
        race_roll = int(input("Too high! Please reroll and enter your new number: "))
    if race_roll in range(1, 10):
        my_race = dndraces[race_roll-1]
    else:
        my_race = random.choice(dndraces)
        
    possible_subraces = dndsubraces[my_race]
    if dndsubracecount[my_race] == 2:
        subrace_roll = input("Roll any die. Is the result odd or even?: ")
        if subrace_roll.lower() == "odd":
            my_subrace = possible_subraces[0]
        elif subrace_roll.lower() == "even":
            my_subrace = possible_subraces[1]
        else:
            my_subrace = random.choice(possible_subraces)
    elif dndsubracecount[my_race] == 3:
        subrace_roll = int(input("Roll a d6. What is your result?: "))
        if subrace_roll == 0:
            my_subrace = random.choice(possible_subraces)
        elif subrace_roll <= 2:
            my_subrace = possible_subraces[0]
        elif subrace_roll <= 4:
            my_subrace = possible_subraces[1]
        else:
            my_subrace = possible_subraces[2]
    print("Your character is a {} {}.".format(my_subrace, my_race))
                
    class_roll = int(input("Next, let's determine your character's class. Roll a d12 and enter the number: "))
    while class_roll > 12:
        class_roll = input("Too high! Please reroll and enter your new number: ")
    if class_roll == 0:
        my_class = random.choice(dndclasses)
    else:
        my_class = dndclasses[class_roll-1]

    possible_subclasses = dndsubclasses[my_class] 
    if dndsubclasscount[my_class] == 2:
        subclass_roll = input("Roll any die. Is the result odd or even?: ")
        if subclass_roll.lower() == "odd":
            my_subclass = possible_subclasses[0]
        elif subclass_roll.lower() == "even":
            my_subclass = possible_subclasses[1]
        else:
            my_subclass = random.choice(possible_subclasses)
    elif dndsubclasscount[my_class] == 3:
        subclass_roll = int(input("Roll a d6. What is your result?: "))
        if subclass_roll == 0:
            my_subclass = random.choice(possible_subclasses)
        elif subclass_roll <= 2: 
            my_subclass = possible_subclasses[0]
        elif subclass_roll <= 4:
            my_subclass = possible_subclasses[1]
        else:
            my_subclass = possible_subclasses[2]
    elif dndsubclasscount[my_class] == 7:
        subclass_roll = int(input("Roll a d8. What is your result?: "))
        while subclass_roll >= 8:
            subclass_roll = int(input("Too high! Roll another d8 and enter the new result: "))
        if subclass_roll == 0:
            my_subclass = random.choice(possible_subclasses)
        else:
            my_subclass = possible_subclasses[subclass_roll - 1]
    elif dndsubclasscount[my_class] == 8:
        subclass_roll = int(input("Roll a d8. What is your result?: "))
        if subclass_roll == 0:
            my_subclass = random.choice(possible_subclasses)
        else:
            my_subclass = possible_subclasses[subclass_roll - 1]

        
    print("You are a {} {}.".format(my_subclass, my_class))

    my_name = input("What would you like to name your character?: ")
    if my_subrace == "none":
        print("Your next D&D character is a {} {} {} named '{}.'".format(my_race, my_subclass, my_class, my_name))
    else:
        print("Your next D&D character is a {} {} {} {} named '{}.'".format(my_subrace, my_race, my_subclass, my_class, my_name))
    redo = input("Would you like to start again? y/n: ").lower()
    if redo == "y": 
        character_builder()
    else:
        print("Thank you for trying out the character randomizer!")

character_builder()

