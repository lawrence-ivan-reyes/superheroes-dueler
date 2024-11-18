class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()
        
        for hero in self.heroes:
            living_heroes.append(hero)
            
        for hero in other_team.heroes:
            living_opponents.append(hero)
        
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero_choice = random.choice(living_heroes)
            opponent_choice = random.choice(living_opponents)
            hero_choice.fight(opponent_choice)
            
            if not hero_choice.is_alive():
                living_heroes.remove(hero_choice)
            
            if not opponent_choice.is_alive():
                living_opponents.remove(opponent_choice)


