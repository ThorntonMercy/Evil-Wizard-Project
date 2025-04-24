import random
from game_logic.character import Character

class Raven(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=18)
        self.bird_strike_cooldown = 0
        self.shadow_form_active = False
        self.shadow_form_turns = 0
        self.shadow_form_cooldown = 0
        
        # Bird strike # deals 2x attack power damage with a 2 turn cooldown
        # Shadow form that heals to full health and increases attack power by 1.5x for 3 turns with a 5 turn cooldown
    def bird_strike(self, opponent):
        if self.bird_strike_cooldown > 0:
            print(f"{self.name} cannot use Bird Strike! {self.bird_strike_cooldown} turns remaining.")
            return

        damage = self.attack_power * 2.0
        print(f"{self.name} uses Bird Strike, dealing {damage:.1f} damage!")
        opponent.take_damage(damage, attacker=self)
        self.bird_strike_cooldown = 2
        
    def shadow_form(self):
        if self.shadow_form_cooldown > 0:
            print(f"{self.name} cannot enter Shadow Form! {self.shadow_form_cooldown} turns remaining.")
            return

        self.shadow_form_active = True
        self.shadow_form_turns = 3
        self.shadow_form_cooldown = 5
        print(f"{self.name} enters Shadow Form for {self.shadow_form_turns} turns!")
        self.health = self.max_health
        print(f"{self.name} fully heals to {self.health}/{self.max_health} HP!")
        self.attack_power *= 1.5
    
    def get_special_moves(self):
        return {"1": "Bird Strike", "2": "Shadow Form"}

    def use_special_move(self, choice, opponent):
        if choice == "1":
            self.bird_strike(opponent)
        elif choice == "2":
            self.shadow_form(opponent)