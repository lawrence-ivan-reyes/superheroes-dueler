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
        total_power = self.starting_health + opponent.starting_health 

        self_win_chance = self.starting_health / total_power

        if random.random() < self_win_chance:
            winner = self
        else:
            winner = opponent

        print(f"{winner.name} defeats {opponent.name if winner == self else self.name}!")

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
        self.current_health -= (damage - defense)

if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(50)
    print(hero.current_health)
    
