import items, enemies, actions, world

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, the_player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles"""
        moves = []
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You manuver your submersible back into section 437 of the Trench. The navigation
        system failed some time ago and your only hope of reaching the surface is to
        follow the labyrinth of underwater veins back to the redevous point.
        
        You can make out four passages, each equally as dark and foreboding.
        """

    def modify_player(self, the_player):
        # Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        In the distance you can make out a bright light.
        You aren't dying. It's the the rendevous point!


        Victory is yours!
        """

    def modify_player(self, the_player):
        the_player.victory = True

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another lifeless portion of the Trench.
        You could really use some sleep.

        You must keep going.
        """

    def modify_player(self, the_player):
        # Room has no action on player
        pass

class GiantCrabRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantCrab())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A prehistoric claw clamps down on your rudder.
            Shaken, you turn around to find a one-armed crab the size of your craft.
            It hasn't eaten in months.
            """
        else:
            return """
            The corpse of the dead crab has already started to vanish.
            """

class SnakePitRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.SnakePit())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Another unremarkable part of the cave. You must forge onwards.
            """
        else:
            return """
            The once crawling pit of snakes is still.
            """

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """

class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        return """
        There are a few old coins sitting on top of a thick dusty book.
        You take them.
        """
