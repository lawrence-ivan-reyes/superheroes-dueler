from ability import Ability
from armor import Armor
from weapon import Weapon
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def fight(self, opponent):
        if not self.abilities and not opponent.abilities:
            print("Draw") 
        else:
            while self.is_alive() and opponent.is_alive():
                hero_attack_damage = self.attack()
                opponent_attack_damage = opponent.attack()
                self.take_damage(opponent_attack_damage)
                opponent.take_damage(hero_attack_damage)

                if self.is_alive() and not opponent.is_alive():
                    print(f"{self.name} won!")
                    self.add_kill(1)
                    opponent.add_death(1)
                elif not self.is_alive() and opponent.is_alive():
                    print(f"{opponent.name} won!")
                    opponent.add_kill(1)
                    self.add_death(1)
                elif not self.is_alive() and not opponent.is_alive():
                    print("Draw!")

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
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
