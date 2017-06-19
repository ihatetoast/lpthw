# * Map
#   - next_scene
#   - opening_scene
# * Engine
#   - play
# * Scene
#   - enter
#   * Death
#   * Central Corridor
#   * Laser Weapon Armory
#   * The Bridge
#   * Escape Pod
from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet config. Subclass it and implement enter()"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name=current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    def enter(self):
        quips = [
            "You died. You're not the brightest star in the galaxy.",
            "Your mom would be proud, but then she drinks a lot.", 
            "Such a sad sack.", 
        ]

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()