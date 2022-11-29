import spacemaths as smaths
import graphicsdefs as graphdefs

class Body:
    ''' Base class for all celestial bodies, though the values don't seem to carry over to inheriting classes '''
    def __init__(self, position:smaths.Vec2):
        self.position = position

class Star(Body):
    ''' Stars inherit from Body, but contain a scale, index, colour, and name '''
    def __init__(self, position:smaths.Vec2, colour:graphdefs.Colour3, scale:float, index:int, name:str):
        self.position = position
        self.colour = colour
        self.scale = scale
        self.index = index
        self.name = name

class Galaxy:
    ''' Galaxies define the star count and contain a list of every star '''
    def __init__(self, star_count:int, star_list):
        self.star_count = star_count
        self.star_list = star_list
