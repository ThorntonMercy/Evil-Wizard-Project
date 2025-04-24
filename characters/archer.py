from game_logic.character import Character 

# ARCHER CLASS
# Special Abilities: 
    # Focus Shot deals 1.5x damage 
    # Acid Spray Shot that gains a barrier for 2 turns

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
        self.barrier_charges = 0

    def focus_shot(self, opponent):
        damage = self.attack_power * 1.5
        print(f"{self.name} uses Focus Shot for {damage:.1f} damage!")
        opponent.take_damage(damage, attacker=self)

    def acid_spray_shot(self, opponent):
        damage = self.attack_power * 1.2
        print(f"{self.name} uses Acid Spray for {damage:.1f} and gains barrier!")
        opponent.take_damage(damage, attacker=self)
        self.barrier_charges = 2

    def take_damage(self, amount, attacker=None):
        if self.barrier_charges > 0:
            print(f"{self.name}'s barrier absorbs half the damage!")
            amount *= 0.5
            self.barrier_charges -= 1
        super().take_damage(amount, attacker)

    def get_special_moves(self):
        return {"1": "Focus Shot", "2": "Acid Spray Shot"}

    def use_special_move(self, choice, opponent):
        if choice == "1":
            self.focus_shot(opponent)
        elif choice == "2":
            self.acid_spray_shot(opponent)