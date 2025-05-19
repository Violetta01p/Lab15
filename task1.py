# Завдання 1: Основний персонаж
class Character:
    def __init__(self, name, level, health, attack):
        self.name = name              # Ім'я персонажа
        self.level = level            # Рівень
        self.health = health          # Здоров'я
        self.attack_power = attack    # Сила атаки

    def show_info(self):
        print(f"Ім'я: {self.name}, Рівень: {self.level}, Здоров'я: {self.health}, Атака: {self.attack_power}")

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакує {other.name} і зменшує здоров'я до {other.health}")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} відновлює здоров'я до {self.health}")


# Завдання 2: Бій між персонажами
hero1 = Character("Герой1", 5, 100, 20)
hero2 = Character("Герой2", 4, 80, 15)

hero1.show_info()
hero2.show_info()
