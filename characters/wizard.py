import random
from game_logic.character import Character

# Special Abilities:
# - Dark Blast that deals 1.0x to 1.4x attack power damage
# - Blazing Inferno that deals 0.5x attack power damage and applies burn to both self and opponent
# - Blight that deals 0.2x to 0.4x attack power damage

class EvilWizard(Character):
    def __init__(self, name="Diablo"):
        super().__init__(name, health=400, attack_power=20)

    def dark_blast(self, opponent):
        damage = self.attack_power * random.uniform(1.0, 1.4)
        damage = round(damage, 1)
        print(f"{self.name} uses Dark Blast for {damage:.1f} damage!")
        opponent.take_damage(damage, attacker=self)
        
    def blight(self, opponent):
        damage = self.attack_power * random.uniform(0.2, 0.4)
        damage = round(damage, 1)
        print(f"{self.name} casts Blight for {damage:.1f} damage!")
        opponent.take_damage(damage, attacker=self)
        
    def blazing_inferno(self, opponent):
        print(f"{self.name} unleashes *Blazing Inferno*!")

        # Deal 0.5x attack power damage to opponent
        damage = round(self.attack_power * 0.5, 1)
        print(f"{self.name} scorches {opponent.name} for {damage:.1f} damage!")
        opponent.take_damage(damage, attacker=self)

        # Apply burn to both self and opponent (kick back damage)
        self.apply_burn()
        opponent.apply_burn()

        # Self-inflicted burn message
        print(f"{self.name} is also burned by the raging inferno!")

    def attack(self, opponent):
        if self.stunned_turns > 0:
            print(f"{self.name} is stunned and skips the turn!")
            self.stunned_turns -= 1
        elif random.random() < 0.4:
            self.dark_blast(opponent)
        else:
            super().attack(opponent)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 HP. Now at {self.health:.1f}/{self.max_health}")
