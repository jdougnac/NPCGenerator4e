import random
from .base import *



class GenerateNPC:
    
    def __init__(self, speciesDef, classDef, genderDef, careerDef, level, books):
        self.npc = {}
        self.genderDef = genderDef
        self.speciesDef = speciesDef
        self.careerFieldDef = classDef
        self.specificCareerDef = careerDef
        self.experience = level
        self.books = books
        character = createCharacter(genderDef, speciesDef, classDef, careerDef, level, books)                
        self.npc['char'] = character
       