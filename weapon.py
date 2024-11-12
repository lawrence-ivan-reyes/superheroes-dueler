from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        half_damage = self.max_damage // 2 
        return random.randint(half_damage, self.max_damage)
