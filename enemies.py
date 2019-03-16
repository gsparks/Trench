class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

class GiantCrab(Enemy):
    def __init__(self):
        super().__init__(name = "Giant Crab", hp = 40, damage = 15)

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name = "Ogre", hp = 30, damage = 15)

class SnakePit(Enemy):
    def __init__(self):
        super().__init__(name = "Snake Pit", hp = 20, damage = 8)
