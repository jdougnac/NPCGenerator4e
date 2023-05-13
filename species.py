import random
from NPCGenerator4e.info import species_selection as spec, career_selection as cs

def assignSpecies(species):
    speciesList = []
    for x in spec.final_species_dict:
        speciesList.append(x)      
    if species == 'random':
        return random.choice(speciesList)
    elif species in speciesList or species in cs.special_species:
        return species
    return 'ERROR'