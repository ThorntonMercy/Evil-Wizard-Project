from game_logic.character import Character
import random

# Warrior Class
# A fierce fighter with powerful melee attacks and special abilities.
# Special Abilities: 
    # Skull Bash that deals 1.5x damage with a 1 turn cooldown
    # Brass Knuckles that deals 0.7x to 1.1x attack power damage based on missing health

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.skull_bash_cooldown = 0

    def skull_bash(self, opponent):
        if self.skull_bash_cooldown > 0:
            print(f"{self.name} can't use Skull Bash yet! ({self.skull_bash_cooldown} turn cooldown)")
            return
        damage = self.attack_power * 1.5
        print(f"{self.name} uses Skull Bash and deals {damage:.1f} damage!")
        opponent.take_damage(damage, attacker=self)
        self.skull_bash_cooldown = 1

    def brass_knuckles(self, opponent):
        missing_health = self.max_health - self.health
        bonus = self.attack_power * (0.01 * missing_health)
        total_attack = self.attack_power + bonus
        damage = round(total_attack * random.uniform(0.7, 1.1), 1)

        print(f"{self.name} activates Brass Knuckles! Missing HP: {missing_health}, "
              f"Bonus Attack: {bonus:.1f}, Total Damage: {damage:.1f}")
        opponent.take_damage(damage, attacker=self)

    def get_special_moves(self):
        return {"1": "Skull Bash", "2": "Brass Knuckles"}

    def use_special_move(self, choice, opponent):
        if choice == "1":
            self.skull_bash(opponent)
        elif choice == "2":
            self.brass_knuckles(opponent)
    
    def end_turn(self):
        if self.skull_bash_cooldown > 0:
            self.skull_bash_cooldown -= 1