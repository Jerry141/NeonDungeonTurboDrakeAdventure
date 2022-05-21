from components.ai import BaseAI, HostileEnemy
from components import consumable
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item


player = Actor(
    char="@", 
    color=(242,34,255), 
    name="Drake", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=30)
)

commoner = Actor(
    char="C", 
    color=(89, 203, 232), 
    name="Commoner", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0)
)
templar = Actor(
    char="T", 
    color=(21, 60, 180), 
    name="Templar", 
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=20, defense=3, power=4),
    inventory=Inventory(capacity=0)
)

health_potion = Item(
    char="!",
    color=(255,41,117),
    name="Neon Blood Vial",
    consumable=consumable.HealingConsumable(amount=4),
)

neon_scroll = Item(
    char="?",
    color=(255,144,31),
    name="Neon Bolt Chip",
    consumable=consumable.NeonDamageConsumable(damage=20, maximum_range=5),
)

confusion_scroll = Item(
    char="?",
    color=(242,34,255),
    name="Confusion Chip",
    consumable=consumable.ConfusionConsumable(number_of_turns=10)
)

neonball_scroll = Item(
    char="?",
    color=(249, 172, 83),
    name="Neonball Chip",
    consumable=consumable.NeonballDamageConsumable(damage=12, radius=3)
)