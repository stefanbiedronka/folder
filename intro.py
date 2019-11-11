import time
import random
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Hero:
    exp_points = 0

    def __init__(self, name, health_points, strength_points, defense_points):
        self.name = name
        self.health_points = health_points
        self.strength_points = strength_points
        self.defense_points = defense_points

    def death(self):
        if self.health_points >= 0:
            print("You are dead!")


Hero1 = Hero("", 100, 0, 0)
Hero1.name = input(delay_print("Welcome to the RPG game! Type in the name of your character: "))
Hero1 = Hero(Hero1.name, 100, 0, 0)

delay_print("Hello " + Hero1.name + "! Time to assign your skill points. "
                        "You have 10 points left. Add points to the following atributes: \nSTRENGTH \nDEFENSE")


Hero1.strength_points = int(input("\nAdd points to strength: "))
spare_points = 10
if Hero1.strength_points > spare_points:
    delay_print("\nYou have only 10 points to assign.")


spare_points = 10 - Hero1.strength_points


Hero1.defense_points = int(input("Add points to defense: "))
if Hero1.defense_points > spare_points:
    delay_print("You have only " + str(spare_points) + " points to assign.")

delay_print(("Well done, %s. You have %d strength points and %d defense points. Let's start the game!" % (Hero1.name,
Hero1.strength_points, Hero1.defense_points)))

time.sleep(4)


class Monster:
    def __init__(self, health_points, strength_points, defense_points):
        self.health_points = health_points
        self.strength_points = strength_points
        self.defense_points = defense_points


Jaszczur = Monster(10, 5, 6)


def fight_monster(monsters_health, monsters_strength, monsters_defense, heroes_health, heroes_strength, heroes_defense):
    delay_print("Fight!")

    keep_on_fighting = True

    while keep_on_fighting:
        if monsters_health <= 0 or heroes_health <= 0:
            keep_on_fighting = False

        delay_print("\nYou attack the monster!")
        attack1 = heroes_strength * random.randint(0, 5) - monsters_defense
        monsters_health -= attack1
        delay_print("\nYou took the monster %d health points!" % attack1)
        delay_print("\nThe monster has %d health points left!" % monsters_health)
        if monsters_health <=0:
            break

        delay_print("\nNow the monster attacks!")
        attack2 = monsters_strength * random.randint(0, 5) - heroes_defense
        heroes_health -= attack2
        delay_print("\nThe monster took you %d health points!" % attack2)
        delay_print("\nYou have %d health points left!" % heroes_health)

    if monsters_health <= 0:
        delay_print("\nYou killed the monster!")
        delay_print("\nYou earned 10 EXP points!")
    elif heroes_health <= 0:
        delay_print("\nYou are dead!")


fight_monster(Jaszczur.health_points, Jaszczur.strength_points, Jaszczur.defense_points, Hero1.health_points, Hero1.strength_points, Hero1.defense_points)



"""
resp = input("You encountered a monster! Do you want to fight or run?")
resp = resp.lower()
if resp 
time.sleep(2)
print("You were too indecisive! The monster attacked you!")
time.sleep(3)
print("Fight now!")
time.sleep(2)

print("Jaszczur has %d health points, kill him!" % Jaszczur.health_points)
attack = random.randint(0, 5) * Hero1.strength_points
time.sleep(3)
print("The attack is taking place now!")
time.sleep(5)

print("Your attack took %d Jaszczur's health points" % attack)

if attack >= Jaszczur.health_points:
    print("You killed Jaszczur! You get 10 EXP points!")
else:
    attack2 = random.randint(0, 5) * Jaszczur.strength_points
    print("Jaszczur took you %d healt points!" % Hero1.health_points)
"""



