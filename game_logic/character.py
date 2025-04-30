import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.stunned_turns = 0  # Stun effect
        self.burn_turns = 0  # Burn effect

    def apply_burn(self):
        self.burn_turns = 3
        print(f"{self.name} is now burning for 3 turns!")

    def take_burn_damage(self):
        if self.burn_turns > 0:
            burn_percent = random.uniform(0.01, 0.05)
            burn_damage = round(self.attack_power * burn_percent, 1)
            self.health -= burn_damage
            self.burn_turns -= 1
            print(f"{self.name} takes {burn_damage:.1f} burn damage! ({self.burn_turns} turns remaining)")

    def attack(self, opponent):
        if self.stunned_turns > 0:
            print(f"{self.name} is stunned and can't attack!")
            self.stunned_turns -= 1
            return
        attack_multiplier = random.uniform(0.6, 1.0)
        damage = round(self.attack_power * attack_multiplier, 1)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        opponent.take_damage(damage, attacker=self)

    def take_damage(self, amount, attacker=None):
        self.health -= amount
        print(f"{self.name} takes {amount:.1f} damage. Remaining health: {self.health:.1f}")

    def attempt_fairy_heal(self, chance=0.1):
        if random.random() <= chance:
            heal_amount = self.max_health * 0.3
            healed = min(heal_amount, self.max_health - self.health)
            if healed > 0:
                self.health += healed
                print(f"Fairy Dust heals {self.name} for {healed:.1f} HP! Now at {self.health:.1f}/{self.max_health}")
            else:
                print(f"Fairy Dust sparkles, but {self.name} is already at full health.")

    def call_for_healing(self):
        missing_health = self.max_health - self.health
        if missing_health <= 0:
            print(f"{self.name} is already at full health!")
            return
        healing_percent = random.uniform(0.1, 0.2)
        heal_amount = min(missing_health * healing_percent, self.max_health - self.health)
        self.health += heal_amount
        self.health = round(self.health, 1)
        print(f"{self.name} calls for healing and restores {heal_amount:.1f} HP! Now at {self.health:.1f}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats ➤ HP: {self.health:.1f}/{self.max_health}, Attack: {self.attack_power}")