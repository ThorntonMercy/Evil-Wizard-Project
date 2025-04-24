from game_logic.character import Character
import random

# Shapeshifter Class
# A mystical creature who transforms under the moonlight, using powerful abilities to heal and stun.
# Special Abilities:
    # Moonlight Slash that fully heals and deals 2.5x attack power damage with a 3 turn cooldown
    # Moon Rising Howl that stuns the opponent for 2 turns

class Shapeshifter(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=18)
        self.moonlight_slash_cooldown = 0  # Cooldown for Moonlight Slash move
        
    def moon_rising_howl(self, opponent):
        print(f"{self.name} howls at the moon! {opponent.name} is stunned for 2 turns!")
        opponent.stunned_turns = 2

    def moonlight_slash(self, opponent):
        if self.moonlight_slash_cooldown > 0:
            print(f"{self.name} cannot use Moonlight Slash! {self.moonlight_slash_cooldown} turns remaining.")
            return

        # Full heal to max health
        self.health = self.max_health
        print(f"{self.name} uses Moonlight Slash and fully heals to {self.health}/{self.max_health} HP!")

        # Critical hit damage (2.5x attack power)
        damage = self.attack_power * 2.5
        damage = round(damage, 1)
        print(f"{self.name} slashes with moonlight, dealing {damage} critical damage!")

        # Apply damage to opponent
        opponent.take_damage(damage, attacker=self)

        # Set cooldown to 3 turns
        self.moonlight_slash_cooldown = 3

    def end_turn(self):
        if self.moonlight_slash_cooldown > 0:
            self.moonlight_slash_cooldown -= 1
            print(f"{self.name}'s Moonlight Slash cooldown is now {self.moonlight_slash_cooldown} turns.")

    def attack(self, opponent):
        if self.stunned_turns > 0:
            print(f"{self.name} is stunned and skips the turn!")
            self.stunned_turns -= 1
        else:
            # Default attack behavior when not using special moves
            attack_multiplier = random.uniform(0.6, 1.0)
            damage = round(self.attack_power * attack_multiplier, 1)
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
            opponent.take_damage(damage, attacker=self)

    def display_stats(self):
        super().display_stats()
        print(f"Moonlight Slash cooldown: {self.moonlight_slash_cooldown}")
        
    def get_special_moves(self):
        return {"1": "Moon Rising Howl", "2": "Moonlight Slash"}

    def use_special_move(self, choice, opponent):
        if choice == "1":
            self.moon_rising_howl(opponent)
        elif choice == "2":
            self.moonlight_slash(opponent)
