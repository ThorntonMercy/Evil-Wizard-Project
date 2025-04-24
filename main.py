from game_logic.create import create_character
from characters.ally import create_random_ally
from characters.wizard import EvilWizard
from game_logic.battle import battle

def main():
    player = create_character()
    ally = create_random_ally()
    print(f"\n {ally.name} is here to help in your battle against the evil wizard!")
    wizard = EvilWizard("Diablo")
    battle(player, ally, wizard)

if __name__ == "__main__":
    main()
