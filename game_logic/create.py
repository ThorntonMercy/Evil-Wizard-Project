from characters.archer import Archer
from characters.mage import Mage
from characters.necromancer import Necromancer
from characters.shapeshifter import Shapeshifter
from characters.warrior import Warrior
from characters.raven import Raven

def create_character():
    print("Choose your class:")
    print("1. Warrior\n2. Mage\n3. Archer\n4. Shapeshifter\n5. Necromancer\n6. Raven")
    
    valid_classes = {'1', '2', '3', '4', '5', '6'}
    choice = ''
    while choice not in valid_classes:
        choice = input("Enter number: ").strip()
        if choice not in valid_classes:
            print("Invalid choice. Please enter a number from 1 to 6.")

    name = input("Enter your name: ").strip()
    if not name:
        name = "Hero"
        print("No name entered. Defaulting to 'Hero'.")

    if choice == '1':
        return Warrior(name)
    elif choice == '2':
        return Mage(name)
    elif choice == '3':
        return Archer(name)
    elif choice == '4':
        return Shapeshifter(name)
    elif choice == '5':
        return Necromancer(name)
    elif choice == '6':
        return Raven(name)