from ability import Ability
from armor import Armor
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        if not self.abilities and not opponent.abilities:
            print("Draw") 

        else:
            while self.is_alive() and opponent.is_alive():

                # stretch: calc damage first
                hero_attack_damage = self.attack()
                opponent_attack_damage = opponent.attack()

                # then apply attacks after
                self.take_damage(opponent_attack_damage)
                opponent.take_damage(hero_attack_damage)

                if self.is_alive() and not opponent.is_alive():
                    print(f"{self.name} won!")
                elif not self.is_alive() and opponent.is_alive():
                    print(f"{opponent.name} won!")
                elif not self.is_alive() and not opponent.is_alive():
                    print("Draw!")
                else:
                    # neither side has lost,so continue the loop
                    continue

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    
    def take_damage(self, damage):
        defense = self.defend()
        actual_damage = damage - defense
        if actual_damage > 0:  
            self.current_health -= actual_damage
    
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
