import random

def battle(player, ally, wizard):
    turn = 1
    while player.health > 0 and wizard.health > 0:
        print(f"\n===== TURN {turn} =====")

        # Apply burn effects
        player.take_burn_damage()
        wizard.take_burn_damage()

        # Player's turn
        print("1. Attack\n2. Special Ability\n3. Fairy Heal\n4. Call for Healing\n5. Stats")
        valid_choices = {'1', '2', '3', '4', '5'}
        choice = ''
        while choice not in valid_choices:
            choice = input("Your action: ").strip()
            if choice not in valid_choices:
                print("Invalid input. Please choose 1–5.")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            special_moves = player.get_special_moves()
            print("\nChoose a special move:")
            for key, move in special_moves.items():
                print(f"{key}. {move}")
            special_keys = set(special_moves.keys())
            special_choice = ''
            while special_choice not in special_keys:
                special_choice = input("Enter number: ").strip()
                if special_choice not in special_keys:
                    print(f"Invalid input. Please choose from: {', '.join(special_keys)}")
            player.use_special_move(special_choice, wizard)
        elif choice == '3':
            player.attempt_fairy_heal()
        elif choice == '4':
            player.call_for_healing()
        elif choice == '5':
            player.display_stats()
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

        if hasattr(player, "end_turn"):
            player.end_turn()

        if hasattr(ally, "end_turn"):
            ally.end_turn()

        turn += 1

    # End of battle
    if player.health <= 0:
        print(f"\n{player.name} was defeated by {wizard.name}!")
    else:
        print(f"\n{player.name} and {ally.name} defeated the evil wizard, {wizard.name}!")
