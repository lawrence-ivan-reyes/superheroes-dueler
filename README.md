# Superhero Dueler 🦸🏻‍♂️
### Ivan Reyes | ACS 1111: Object Oriented Programming | Dani Roxberry

---

### ℹ️ Program Description
Superhero Dueler is an interactive CLI game where teams of superheroes battle it out. Customize teams with unique abilities, weapons, and armor. This program highlights the principles of object-oriented programming.

**Key Features:**
- **Team Building**: Create and customize teams with heroes having unique abilities, weapons, and armor.
- **Dynamic Battles**: Heroes engage in battles based on their attributes, leading to various outcomes.
- **Stat Tracking**: Keep track of kills, deaths, and average kill/death ratios for each hero.
- **Replayability**: Easily reset heroes' health and play multiple battles with the same teams.

---

### ❗️ How To Use
1. **Clone the repository:**
- **HTTPS**: `git clone https://github.com/lawrence-ivan-reyes/superheroes-dueler.git`  
- **SSH**: `git clone git@github.com:lawrence-ivan-reyes/superheroes-dueler.git`  
- **GitHub CLI**: `gh repo clone lawrence-ivan-reyes/superheroes-dueler` 

2. **Run the Program:** `python3 arena.py`

3. **Game Controls:** Simply follow on-screen prompts to create teams and control the game flow.

---

### 💻 Code Structure
**Main Game Files**
- `arena.py`: Contains the `Arena` class to manage teams, battles, and game flow.
- `hero.py`: Contains the `Hero` class with methods for battling, tracking stats, and managing abilities.
- `team.py`: Contains the `Team` class for managing groups of heroes and conducting team battles.

**Supporting Files**
- `ability.py`: Contains the `Ability` class for hero abilities.
- `armor.py`: Contains the `Armor` class for hero armor.
- `weapon.py`: Contains the `Weapon` class, inherited from `Ability`, for hero weapons.
