from monster import Monster

hit_points = 1
color = 'yellow'
weapon = 'sword'
sound = 'tweet'

print("Jub Jub")
jubjub = Monster(color='red', sound = 'tweet')

print(jubjub.hit_points)
print(jubjub.battlecry())

print("Ogre")

ogre = Monster(hit_points=10)
print(ogre.hit_points)
print(ogre.battlecry())
