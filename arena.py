from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("What is the ability name? ")
        max_damage = int(input("What is the max damage of the ability? "))
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name? ")
        max_damage = int(input("What is the max damage of the weapon? "))
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armor name? ")
        max_block = int(input("What is the max block of the armor? "))
        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        self.team_one = Team(input("Enter Team One name: "))
        num_of_team_members = int(input("How many members would you like on Team One?\n"))
        for _ in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        self.team_two = Team(input("Enter Team Two name: "))
        num_of_team_members = int(input("How many members would you like on Team Two?\n"))
        for _ in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        team_one_kills = sum(hero.kills for hero in self.team_one.heroes)
        team_one_deaths = sum(hero.deaths for hero in self.team_one.heroes) 
        print(f"{self.team_one.name} average K/D was: {team_one_kills/team_one_deaths}")

        team_two_kills = sum(hero.kills for hero in self.team_two.heroes)
        team_two_deaths = sum(hero.deaths for hero in self.team_two.heroes) 
        print(f"{self.team_two.name} average K/D was: {team_two_kills/team_two_deaths}")

        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(f"Survived from {self.team_one.name}: {hero.name}")

        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(f"Survived from {self.team_two.name}: {hero.name}")

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

    def edit_teams(self):
        while True:
            print("\nEditing Options:")
            print("[1] Rebuild Team One")
            print("[2] Rebuild Team Two")
            print("[3] Done Editing\n")
            choice = input("Choose an option: ")

            if choice == "1":
                self.team_one = self.build_team(input("Enter new Team One name: "))
            elif choice == "2":
                self.team_two = self.build_team(input("Enter new Team Two name: "))
            elif choice == "3":
                break
            else:
                print("Invalid choice, please choose again.")

if __name__ == "__main__":
    game_is_running = True

    arena = Arena()

    while game_is_running:
        print("\nMain Menu:")
        print("[1] Build Teams")
        print("[2] Edit Teams")
        print("[3] Start Battle")
        print("[4] Exit\n")
        choice = input("Choose an option: ")

        if choice == "1":
            arena.build_teams()
        elif choice == "2":
            arena.edit_teams()
        elif choice == "3":
            arena.team_battle()
            arena.show_stats()
            play_again = input("Play Again? Y or N: ")

            if play_again.lower() == "n":
                game_is_running = False
            else:
                arena.team_one.revive_heroes()
                arena.team_two.revive_heroes()
        elif choice == "4":
            game_is_running = False
        else:
            print("Invalid choice, please choose again.")
