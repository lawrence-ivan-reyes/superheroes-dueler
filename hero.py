import random

class Hero:
    def __init__(self, name, starting_health=100):
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

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman", 300)
    hero2 = Hero("Dumbledore", 250)
    hero1.fight(hero2)
