from monster import Goblin
from monster import Dragon
from monster import Troll
from character import Character

player = Character()
print(player)
print('Attack: {}'.format(player.attack()))
print('Dodge: {}'.format(player.dodge()))

print(">>> azog <<<")
azog = Goblin()
print(azog)
print('Attack: {}'.format(azog.attack()))
print('Dodge: {}'.format(azog.dodge()))

print(">>> snaga <<<")
snaga = Troll()
print(snaga)
print('Attack: {}'.format(snaga.attack()))
print('Dodge: {}'.format(snaga.dodge()))

print(">>> pete <<<")
pete = Dragon()
print(pete)
print('Attack: {}'.format(pete.attack()))
print('Dodge: {}'.format(pete.dodge()))
