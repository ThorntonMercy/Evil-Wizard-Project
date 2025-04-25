import random
from characters.warrior import Warrior
from characters.mage import Mage
from characters.archer import Archer
from characters.shapeshifter import Shapeshifter
from characters.necromancer import Necromancer
from characters.raven import Raven

# A randomly generated ally to assist the player in taking down the evil wizard.

def create_random_ally(player):
    ally_classes = [Warrior, Mage, Archer, Shapeshifter, Necromancer, Raven]
    ally_classes.remove(player.__class__)  # Ensure the ally is not the same class as the player
    AllyClass = random.choice(ally_classes)
    ally_name = random.choice(["Lyra", "Finn", "Kestrel", "Nyx", "Fenrir", 
                               "Marva", "Merlin", "Sable", "Rune", "Feather"])
    return AllyClass(f"{ally_name} your {AllyClass.__name__} ally")
