import random
from characters.mage import Mage
from characters.warrior import Warrior
from characters.archer import Archer
from characters.shapeshifter import Shapeshifter
from characters.necromancer import Necromancer


# def battle(player, ally, wizard):
#     turn = 1
#     while player.health > 0 and wizard.health > 0:
#         print(f"\n===== TURN {turn} =====")
        
#         # Apply burn effects
#         player.take_burn_damage()
#         wizard.take_burn_damage()

#         print("1. Attack\n2. Special Ability\n3. Fairy Heal\n4. Call for Healing\n5. Stats")
#         choice = input("Your action: ")

#         if choice == '1':
#             player.attack(wizard)
#         elif choice == '2':
#             special_moves = player.get_special_moves()
#     print("\nChoose a special move:")
#     for key, move in special_moves.items():
#         print(f"{key}. {move}")
#     special_choice = input("Enter number: ")
#     player.use_special_move(special_choice, wizard)
                
#                 # Other generic move choices
#     elif choice == '3':
#         player.attempt_fairy_heal()
#     elif choice == '4':
#         player.call_for_healing()
#     elif choice == '5':
#         player.display_stats()
#         continue
#     else:
#         print("Invalid input. Try again.")
            
            
#         if wizard.health > 0:
#             wizard.regenerate()

#             # Choose randomly between spells including blazing_inferno
#             move = random.choice(["attack", "dark_blast", "blight", "blazing_inferno"])
#             if move == "dark_blast":
#                 wizard.dark_blast(player)
#             elif move == "blight":
#                 wizard.blight(player)
#             elif move == "blazing_inferno":
#                 wizard.blazing_inferno(player)
#             else:
#                 wizard.attack(player)

#         turn += 1
        
#         # Ally takes turn after player
#         if ally.health > 0:
#             print(f"\n {ally.name}'s turn!")
            
#             if isinstance(ally, Mage) and random.random() < 0.3:
#                 ally.stargaze(wizard)
#             elif isinstance(ally, Warrior) and random.random() < 0.3:
#                 ally.skull_bash(wizard)
#             elif isinstance(ally, Archer) and random.random() < 0.3:
#                 ally.acid_spray_shot(wizard)
#             elif isinstance(ally, Necromancer) and random.random() < 0.2:
#                 ally.grave_bust(wizard)
#             elif isinstance(ally, Shapeshifter) and random.random() < 0.2:
#                 ally.moon_rising_howl(wizard)
#             else:
#                 ally.attack(wizard)

#     # End of battle
#     if player.health <= 0:
#         print(f"\n{player.name} was defeated by {wizard.name}!")
#     else:
#         print(f"\n {player.name} defeats the evil wizard {wizard.name}!")

def battle(player, ally, wizard):
    turn = 1
    while player.health > 0 and wizard.health > 0:
        print(f"\n===== TURN {turn} =====")
        
        # Apply burn effects
        player.take_burn_damage()
        wizard.take_burn_damage()

        # Player's turn
        print("1. Attack\n2. Special Ability\n3. Fairy Heal\n4. Call for Healing\n5. Stats")
        choice = input("Your action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            special_moves = player.get_special_moves()
            print("\nChoose a special move:")
            for key, move in special_moves.items():
                print(f"{key}. {move}")
            special_choice = input("Enter number: ")
            player.use_special_move(special_choice, wizard)
        elif choice == '3':
            player.attempt_fairy_heal()
        elif choice == '4':
            player.call_for_healing()
        elif choice == '5':
            player.display_stats()
            continue
        else:
            print("Invalid input. Try again.")
            continue

        # Wizard's turn
        if wizard.health > 0:
            wizard.regenerate()
            move = random.choice(["attack", "dark_blast", "blight", "blazing_inferno"])
            if move == "dark_blast":
                wizard.dark_blast(player)
            elif move == "blight":
                wizard.blight(player)
            elif move == "blazing_inferno":
                wizard.blazing_inferno(player)
            else:
                wizard.attack(player)

        # Ally's turn
        if ally.health > 0 and wizard.health > 0:
            print(f"\n{ally.name}'s turn!")
            if hasattr(ally, 'get_special_moves') and hasattr(ally, 'use_special_move'):
                special_moves = ally.get_special_moves()
                if special_moves and random.random() < 0.5:
                    special_choice = random.choice(list(special_moves.keys()))
                    ally.use_special_move(special_choice, wizard)
                else:
                    ally.attack(wizard)
            else:
                ally.attack(wizard)

        turn += 1

    # End of battle
    if player.health <= 0:
        print(f"\n{player.name} was defeated by {wizard.name}!")
    else:
        print(f"\n{player.name} and {ally.name} defeated the evil wizard, {wizard.name}!")
