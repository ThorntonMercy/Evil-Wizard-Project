from game_logic.character import Character

# MAGE CLASS
# Special Abilities: 
# Stargaze deals 3x damage but kicks back a stun for 1 turn 
# Disguise (hidden from damage and heals). 
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        self.disguised = False

    def stargaze(self, opponent):
        if self.stunned_turns > 0:
            print(f"{self.name} is stunned and can't cast Stargaze!")
            return
        damage = self.attack_power * 3
        print(f"{self.name} casts Stargaze and deals {damage:.1f} damage!")
        opponent.take_damage(damage, attacker=self)
        self.stunned_turns = 1
        print(f"{self.name} is stunned by magic backlash and will miss next turn!")

    def disguise(self):
        if self.disguised:
            print(f"{self.name} is already hidden!")
            return
        self.disguised = True
        heal = self.max_health * 0.05
        self.health = min(self.max_health, self.health + heal)
        print(f"{self.name} casts Disguise and heals {heal:.1f}. Next attack will miss!")

    def take_damage(self, amount, attacker=None):
        if self.disguised:
            print(f"{self.name} dodges the attack due to Disguise!")
            self.disguised = False
            return
        super().take_damage(amount, attacker)

    def get_special_moves(self):
        return {"1": "Stargaze", "2": "Disguise"}

    def use_special_move(self, choice, opponent):
        if choice == "1":
            self.stargaze(opponent)
        elif choice == "2":
            self.disguise()