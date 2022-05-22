# Neon Dungeon Turbo Drake Adventure

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Content](#content)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Manual](#manual)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- Neon Dungeon Turbo Drake Adventure (NDTDA) is a Rogue Like inspired by no other game than Rogue itself, Synthwave and Vampires.
- You play as the Turbo Drake - manifestation of Vlad Drakula Tepesh in the Synthwave inspired world where Neons are the source of power.
- The lower you go through the dungeon the more dangerous it gets, be ready to get more powerful as well by feeding upon the enemies residing this wretched place.
- The game is in very early stages of development, but content is planned to be added as frequent as possible, as this is my side project and I have no time or resources to commit to this 100% unfortunately.


## Technologies Used
Python 3.10

- cffi==1.15.0
- numpy==1.22.3
- pycparser==2.21
- tcod==13.6.2
- typing_extensions==4.2.0


## Content
Content already in the game:

Enemies:
- Commoner [C] - Low class human, for some reason there are many of them in the dungeon. They posses no real threat, easy prey for Drake.
- Templar [T] - Templars are assigned by the Neon Church to protect the Commoners inside the dungeon, the lower you go the more you will encounter them, looks like they do not bother about the entrance anymore. Fairly powerful beings.
- Vampire Hunter [H] - Hunters set by the Neon Church to eradicate Vampires searching the dungeon for Neon Power. Well trained and viscious against their target, even with low defenses, they are a big threat to any Vampire deciding to venture through the Dungeon.
- Neon Addict [a]- Neon addicts are mostly commoners who were exposed to the Neon for so long that they have lost their mind and the only thing they want is to get more Neon. They are very vulnerable but due to huge exposure to the Neon, they are very strong and should be erradicated before they have a chance to attack. 

Items:
- Neon Blood Vial [!] - Blood Vial contaminated by the large amount of Neon - for mere human it is like a drug, easy to get addicted to it and loose sanity trying to find more and more. For Drake, it is great source of Health, fantastic to regain Vitals before next fights.
- Neon Bolt Chip [~] - This Chip contains technology to cast Neon Bolt, harming enemies by dealing them massive damage.
- Confusion Chip [~] -  This Chip contains technology to cast Confusion "spell", making enemies lose their mind for a brief moment.
- Neonball Chip [~] - This Chip contains technilogy on how to cast Neonball, powerfull AoE spell, dealing damage on fairly wide range.

Equipment:
- Neon Dagger [/] - Simple dagger infused with Neon, probably due to long exposure within the dungeon. Great for dealing with small threats
- Neon Saber [/] - Saber greatly infused with Neon, can be found in lower levels of the dungeon, probably was used by previous residents of this place, an elegant weapon for a more civilized age.
- Light Armor [ [ ] - Light armor, providing small amount of defense, but even that is better than nothing and can save your life.
- Medium Armor [ [ ] - Medium armor, providing moderate amount of defense, great for more powerful enemies.


## Screenshots
Screenshots - TBA


## Setup
Currently only Windows version is working. To download exe just follow [this link](https://mega.nz/file/D65T0S6b#Bteg84CJm4iSZ6A2KUwNtizuFDb8lYrOiF48fwCzdy4)
Extract the files and run `main.exe`

The other solution is to download the files from repository.
Make sure you have Python 3.x.x installed.

Install the required libs:
`pip install -r requirements.txt`

Then just run main.py
`python main.py`


## Manual

Neon Dungeon is a very dangerous place, therefor it is nice to know how to move around this wretched place.

Game auto saves after quitting the game. There is only one save slot for now and it resets after death.

### Key Bindings:

You can either use arrow keys, numpad or Vi keys for movement:
- UP - [Arrow Key Up] / [Numpad_8] / [k]
- DOWN - [Arrow Key Down] / [Numpad_2] / [j]
- LEFT - [Arrow Key Left] / [Numpad_4] / [h]
- RIGHT - [Arrow Key Right] / [Numpad_6] / [l]
- UP/LEFT (Diagonal) - [HOME] / [Numpad_7] / [y]
- UP/RIGHT (Diagonal) - [PAGE_UP] / [Numpad_9] / [u]
- DOWN/LEFT (Diagonal) - [END] / [Numpad_1] / [b]
- DOWN/RIGHT (Diagonal) - [PAGE_DOWN] / [Numpad_3] / [n]

Inventory:
- Open Inventory - [i]
- Use Items - [a-u]
- Drop Items Menu - [d]
- Drop Items from Drop Item Menu - [a-u]
- Pick Up Item - [g]

- Go to the next level - [Shift + .] 
- Look Up (provides the ability to check the enviorment using the keyboard) - [/]
- Open message log - [v]

- Close game - [ESC]

### Combat:
The Combat in NDTDA is turn based. Once player moves/pick up items/uses item it counts as a turn. After that every enemy on the map (if visible) takes their turn to get close to the player and attack them.

Attacking is done by moving into the enemy, same comes from the enemies. Attack can be done from 8 directions - Horizontaly, Vertically and Diagonaly.

Using Chips - to use the spell you need to go to inventory [i] and select the Chip:
- Neon Bolt Chip - attacks for 20 damage, max range is 5 dots. Targets the closest enemy.
- Confusion Chip - deals no damage, confuses the enemy, targetable - target must be visible and cannot be the player, confusion effect lasts for 10 turns.
- Neonball Chip - deals 12 damage within the radius of 3x3 dots. Targetable, can deal damage to the player if within the radius.

### Equipment:
There are currently 2 types of equipment: Armor and Weapon.

To equip gear you need to go into the Inventory [i] and select equipment to equip, in the inventory you will notice (E) next to the equipment if equiped.

You can have only 1 of each type equiped.

In Game there are currently the following equipment items:

Weapons:
- Neon Dagger - adds 2 power - starting weapon
- Neon Saber - adds 4 power

Armor:
- Light Armor - adds 1 defense - starting armor
- Medium Armor - adds 3 defense


## Project Status
Project is: _in progress_


## Room for Improvement

Room for improvement:
- Add mouse controls to the interface
- Improve the Inventory to be less messy (Sorting and stacking)

To do:
- Add more enemies
- Add bosses
- Add more Consumables
- Add more Equippable items (Weapon and Armor)


## Acknowledgements
- This project was inspired by Rogue: Exploring the Dungeons of Doom
- This project was based on [this tutorial](https://rogueliketutorials.com/tutorials/tcod/v2/).
- Main Menu background - found in google, unfortunately I forgot to write down the author, so if you find it somehow please let me know so I can properly mentioned them. For now it is only a placeholder but I really like it so it would be nice to keep it as is.


## Contact
Created by [@JayJayJerry](https://www.facebook.com/jayjayjerrygaming) - feel free to contact me!
