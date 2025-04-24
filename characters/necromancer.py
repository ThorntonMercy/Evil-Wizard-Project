import random
from game_logic.character import Character

# Special Abilities:
# Grave Bust that deals 1.4x of attack power with a 40% chance
# Raise Hell that deals a flat 25 damage with a 25% chance of triggering. 

class Necromancer(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=22)

    def grave_bust(self, opponent):
        if random.random() <= 0.4:
            damage = self.attack_power * 1.4
            print(f"{self.name} performs a Grave Bust for {damage:.1f}!")
            opponent.take_damage(damage, attacker=self)
        else:
            print(f"{self.name}'s Grave Bust failed.")
        
        # Chance to trigger Raise Hell move (25% chance)
        if random.random() <= 0.25:
            self.raise_hell(opponent)

    def raise_hell(self, opponent):
        damage = 25
        print(f"{self.name} raises hell and deals {damage} damage!")
        opponent.take_damage(damage, attacker=self)

    def get_special_moves(self):
        return {"1": "Grave Bust", "2": "Raise Hell"}

    def use_special_move(self, choice, opponent):
        if choice == "1":
            self.grave_bust(opponent)
        elif choice == "2":
            self.raise_hell(opponent)