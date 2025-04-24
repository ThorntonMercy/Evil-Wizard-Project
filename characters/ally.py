import random
from characters.warrior import Warrior
from characters.mage import Mage
from characters.archer import Archer
from characters.shapeshifter import Shapeshifter
from characters.necromancer import Necromancer
from characters.raven import Raven

# Randomly assigned an ally to help fight the wizard
def create_random_ally():
    ally_classes = [Warrior, Mage, Archer, Shapeshifter, Necromancer, Raven]
    AllyClass = random.choice(ally_classes)
    ally_name = random.choice(["Lyra", "Finn", "Kestrel", "Nyx", "Fenrir", 
                               "Marva", "Merlin", "Sable", "Rune", "Feather"])
    return AllyClass(f"{ally_name}")
