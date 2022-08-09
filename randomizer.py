import random

dndraces = ["dwarf", "elf", "halfling", "human", "dragonborn", "gnome", "half-elf", "half-orc", "tiefling"]

dndsubraces = {"dwarf": ["hill", "mountain"], "elf": ["high", "wood", "dark"], "halfling": ["lightfoot", "stout"], "human": ["standard", "variant"], "dragonborn": "", "gnome": ["forest", "rock"], "half-elf": "", "half-orc": "", "tiefling": ""}

dndclasses = {"barbarian": ["Path of the Berserker", "Path of the Totem Warrior"], "bard": ["College of Lore", "College of Valor"], "cleric": ["Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Tempest Domain", "Trickery Domain", "War Domain"], "druid": ["Circle of the Land", "Circle of the Moon"], "fighter": ["Champion", "Battle Master", "Eldritch Knight"], "monk": ["Way of the Open Hand", "Way of Shadow", "Way of the Four Elements"], "paladin": ["Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance"], "ranger": ["Hunter", "Beast Master"], "rogue": ["Thief", "Assassin", "Arcane Trickster"], "sorcerer": ["Draconic Bloodline", "Wild Magic"], "warlock": ["Archfey", "Fiend", "Great Old One"], "wizard": ["Abjuration", "Conjuration", "Divination", "Enchantment", "Evocation", "Illusion", "Necromancy", "Transmutation"]}

my_race = ""
my_subrace = ""
my_class = ""
my_subclass = ""

print("Hello! Welcome to the D&D random character generator.")
while my_race == "":
    race_key = int(input("First, let's determine your character's race. Roll a d10 and enter the number, or enter '0' if you would like us to roll for you: "))
    while race_key >= 10:
        race_key = input("Too high! Please reroll and enter your new number: ")
    if race_key in range(1, 10):
        my_race = dndraces[race_key-1]
    elif race_key.lower() == "random":
        my_race = random.choice(dndraces)
    else:
        print("Please try again. Make sure you input a number between 1 and 10 or the word 'random' to continue: ")
    
while my_subrace == "":
    if len(dndsubraces[my_race].values()) == 1:
        my_subrace = "none"
        print("Your character is a {}".format(my_race))
    elif len(dndsubraces[my_race].values()) == 2:
        possible_subraces = dndsubraces[my_race]
        subrace_roll = input("Roll any die. Is the result odd or even?: ")
        if subrace_roll.lower() == "odd":
            my_subrace = possible_subraces[0]
        else:
            my_subrace = possible_subraces[1]
        print("Your character is a {} {}.".format(my_subrace, my_race))
    else:
        possible_subraces = dndsubraces[my_race]
        subrace_roll = int(input("Roll a d6. What is your result?: "))

        
        

