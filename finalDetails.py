import random
from NPCGenerator4e.info.final_details import *

def retrieveAge(species):
    if species == 'human' or ' human' in species:
        age = 15 + random.randint(1,10)
    elif species == 'dwarf':
        age = 15
        for item in range(0,10):
            age += random.randint(0,10)
    elif species == 'halfling':
        age = 15
        for item in range(0,5):
            age += random.randint(0,10)       
    elif ' elf' in species:
        age = 30
        for item in range(0,10):
            age += random.randint(0,10)
    elif ' familiar' in species:
        age = 1
        for item in range(0,5):
            age += random.randint(0,5)
    return age

def retrieveEyeColour(species):
    if ' human' in species:
        species = 'human'
    eyeColour = random.choice(eye_colour[species])
    return eyeColour

def retrieveHairColour(species):
    if ' human' in species:
        species = 'human'
    hairColour = random.choice(hair_colour[species])
    return hairColour


def retrieveHeight(species):
    if ' human' in species:
        species = 'human'    
    baseHeight = heights[species].copy()
    addedHeight = random.randint(1,10)
    if species == 'human':
        addedHeight += random.randint(1,10)         
    baseHeight[1] += addedHeight

    extraFeet = baseHeight[1]//12
    baseHeight[0] += extraFeet
    baseHeight[1] -= extraFeet * 12
    
    finalHeight = str(baseHeight[0]) + "'" + str(baseHeight[1]) + '"'
    return finalHeight

