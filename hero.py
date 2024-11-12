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
    

if __name__ == "__main__":
  ability = Ability("Great Debugging", 50)
  hero = Hero("Grace Hopper", 200)
  hero.add_ability(ability)
  print(hero.abilities)
