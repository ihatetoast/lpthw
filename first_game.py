from sys import exit
from random import randinit

class Engine(object)
    def __init__(self, scene_map):
        pass
    def play(self):
        pass

class Scene(object):
    def enter(self):
        pass

class DayRuined(Scene):
    sledges = [
        "You stepped in poop. Your day is ruined.",
        "You accidentally wiped your forehead with the poop bag. Your day is ruined.",
        "You slipped on poop and fell on it. Your day is ruined",
        "The bag ripped and poop fell onto your feet. Your day is ruined."
    ]
    def enter(self):
        print DayRuined.sledges[randint(0, len(self.sledges)-1]
        exit(1)

class LivingRoom(Scene):
    def enter(self):
        pass

class PooBags(Scene):
    def enter(self):
        pass

class BackYard(Scene):
    def enter(self):
        pass

class WheelieBin(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass

    def __init__(self, scene_name):
        pass

    def opening_scene(self):
        pass

scoop_map = Map('central_corridor')
scoop_game = Engine(scoop_map)
scoop_game.play()

