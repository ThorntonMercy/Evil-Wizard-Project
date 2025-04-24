from characters.archer import Archer
from characters.mage import Mage
from characters.necromancer import Necromancer
from characters.shapeshifter import Shapeshifter
from characters.warrior import Warrior

def create_character():
    print("Choose your class:")
    print("1. Warrior\n2. Mage\n3. Archer\n4. Shapeshifter\n5. Necromancer")
    choice = input("Enter number: ")
    name = input("Enter your name: ")

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
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)