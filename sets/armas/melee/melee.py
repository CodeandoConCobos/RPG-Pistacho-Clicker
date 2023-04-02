import random

class Weapon:
    def __init__(self, name, attack, durability=100):
        self.name = name
        self.attack = attack
        self.durability = durability
    
    def attack(self):
        print(f"{self.name} usó {self.attack}!")

class Puños(Weapon):
    def __init__(self, hijo):
        super().__init__("Puños", hijo.daño_base + random.randint(1,3), durability=100)
        self.fail_chance = random.uniform(0.2, 0.3)  # 20% - 30% de probabilidad de fallar
        self.crit_chance = random.uniform(0.015, 0.02)  # 1.5% - 2% de probabilidad de golpe crítico
        
    def attack(self):
        if random.random() < self.fail_chance:  # Comprobar si el ataque falla
            print(f"{self.name} al usar Puños falló!")
            return
        
        crit_multiplier = 1.5 if random.random() < self.crit_chance else 1  # Multiplicador crítico de 1 o 1.5
        total_attack = self.attack * self.durability / 100 * crit_multiplier
        
        if crit_multiplier > 1:
            print(f"{self.name} ataca con sus Puños y realizó un golpe crítico, haciendo {total_attack} de daño!")
            self.durability -= 0
        else:
            print(f"{self.name} ataca con sus Puños e hizo {total_attack} de daño!")
            self.durability -= 0
        
class PaloDeMadera(Weapon):
    def __init__(self, hijo):
        super().__init__("Palo de Madera", hijo.daño_base + random.randint(3,7), durability=100)
        self.fail_chance = random.uniform(0.15, 0.25)  # 15% - 25% de probabilidad de fallar
        self.crit_chance = random.uniform(0.025, 0.03)  # 2.5% - 3% de probabilidad de golpe crítico
        
    def attack(self):
        if random.random() < self.fail_chance:  # Comprobar si el ataque falla
            print(f"{self.name} al usar Palo de Madera falló!")
            return
        
        total_attack = self.attack * self.durability / 100
        crit_multiplier = 1.5 if random.random() < self.crit_chance else 1  # Multiplicador crítico de 1 o 1.5
        total_attack *= crit_multiplier
        
        if crit_multiplier > 1:
            print(f"{self.name} ataca con su Palo de Madera y realizó un golpe crítico, haciendo {total_attack} de daño!")
            self.durability -= 2
        else:
            print(f"{self.name} ataca con su Palo de Madera e hizo {total_attack} de daño!")
            self.durability -= 1

