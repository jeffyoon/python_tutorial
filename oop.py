# -*- coding: utf-8 -*-

# Define the Class
class Character(object):
    '''
    Define the Character class object to make a game character.
    Character class has a name, health, damage, inventory
    '''
    def __init__(self, name, health, damage, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = inventory

    def __repr__(self):
        return self.name

# Create an object(instance) of Character class.
heroes = []
heroes.append(Character('아이어맨', 100, 200, {'gold': 500, 'weapon': '레이저'}))
heroes.append(Character('데드폴', 300, 50, {'gold': 300, 'weapon': '장검'}))
heroes.append(Character('울버린', 200, 100, {'gold': 200, 'weapon': '클로'}))

monsters = []
monsters.append(Character('고블린', 90, 30, {'gold': 50, 'weapon': '창'}))

print(heroes)
print(monsters)
del heroes[0]
print(heroes)
