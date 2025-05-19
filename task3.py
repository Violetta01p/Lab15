# Базовий клас
class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def info(self):
        print(f"{self.name} | Рівень: {self.level}, Здоров'я: {self.health}, Атака: {self.attack}")

    def restore_health(self):
        self.health += 20
        print(f"{self.name} відновив 20 здоров'я. Нове здоров'я: {self.health}")

# Підкласи з унікальними властивостями
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, level=3, health=150, attack=30)
        self.shield = True  # Унікальна властивість

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, level=2, health=80, attack=40)
        self.mana = 100  # Унікальна властивість

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, level=2, health=90, attack=25)
        self.arrows = 10  # Унікальна властивість

# Створення героїв
w = Warrior("Воїн")
m = Mage("Маг")
a = Archer("Лучник")

# Вивід інформації та відновлення здоров'я
w.info()
m.restore_health()
