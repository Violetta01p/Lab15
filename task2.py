# Продовжуємо працювати з класом Character

class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def info(self):
        print(f"{self.name} | Рівень: {self.level}, Здоров'я: {self.health}, Атака: {self.attack}")

    def attack_enemy(self, other):
        # Атакує іншого персонажа, зменшуючи його здоров'я
        print(f"{self.name} атакує {other.name} на {self.attack} одиниць")
        other.health -= self.attack

# Створення двох персонажів
hero1 = Character("Лицар", 2, 120, 25)
hero2 = Character("Монстр", 1, 100, 15)

# Бій
hero1.attack_enemy(hero2)
hero2.info()
