import random
from NPCGenerator4e.info import species_selection


def generateBaseAttributes():
    attributeList = []
    for x in range(0,10):
        firstDie = random.randint(1,10)
        secondDie = random.randint(1,10)
        attributeList.append(firstDie + secondDie)
    return attributeList

def generateFate(species):
    otherAttributes = species_selection.final_species_dict[species]['stats'][10:12]
    bonusPoints = species_selection.final_species_dict[species]['stats'][12] 
    for x in range(0, bonusPoints):
        otherAttributes[random.randint(0,1)] += 1
    return otherAttributes

def generateMovement(species):
    return species_selection.final_species_dict[species]['stats'][-1]

def generateStartingAttributes(species):
    baseAttributes = generateBaseAttributes()
    speciesAttributes = species_selection.final_species_dict[species]['stats'][:]
    for item in range(0,10):
        speciesAttributes[item] += baseAttributes[item]    
    return speciesAttributes

def generateWounds(species, strength, toughness, willpower):
    sb = strength//10
    tb = toughness//10
    wpb = willpower//10
    if species in ['halfling', 'combat familiar','spell familiar']:
        wounds = (2*tb)+wpb
    else:
        wounds = sb+(2*tb)+wpb
    return wounds