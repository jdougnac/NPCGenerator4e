from NPCGenerator4e.info import career_selection as cs
import copy
import random

def filterCareerBySpecies(species):
    start_careers = copy.deepcopy(cs.careers)
    if species in cs.special_species:
        start_careers = cs.special_species[species]
    elif ' human' in species:
        species = 'human'
    else:    
        for x in cs.forbidden_careers[species]:       
            for item in cs.forbidden_careers[species][x]:  
                if item in start_careers[x]:
                    start_careers[x].remove(item)

    return start_careers


def pickCareer(species,gameClass,career):
    careerFiltered = filterCareerBySpecies(species)
    if species in cs.special_species and career == 'random' and gameClass == 'random':
        finalCareer = random.choice(cs.special_species[species])
    elif species in cs.special_species and career == 'random' and gameClass != 'random':
        finalCareer = random.choice(cs.careers[gameClass])
    elif career != 'random':
        return career
    elif gameClass != 'random':
        finalCareer = random.choice(careerFiltered[gameClass])
    else:
        finalClass = random.choice(list(careerFiltered.values()))
        finalCareer = random.choice(finalClass)
    return finalCareer