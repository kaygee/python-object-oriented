from combat import Combat
import random

class Character(Combat):
    xp = 0
    base_hp = 10
    attack_limit = 10

    def get_weapon(self):
        weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow): ").lower()

        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'sword'
            elif weapon_choice == 'a':
                return 'axe'
            else:
                return 'bow'
        else:
            return self.get_weapon()

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 2
        return roll > 4

    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.__class__.__name__, self.name, self.hp, self.xp)

    def rest(self):
        if self.hp < self.base_hp:
            self.hp += 1

    def lvl_up(self):
        return self.xp >= 5

    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.weapon = self.get_weapon()
        self.hp = self.base_hp

        for key, value in kwargs.items():
            setattr(self, key, value)
