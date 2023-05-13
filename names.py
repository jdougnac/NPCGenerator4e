import random
from NPCGenerator4e.info.name_info import *

def retrieveReiklanderName(gender):
    if gender == 'male':
        first_name = random.choice(reiklander_male_first_name)
    elif gender == 'female':
        first_name = random.choice(reiklander_female_first_name)
    family_name = random.choice(reiklander_family_names)
    final_name = first_name + " " + family_name
    return final_name

def retrieveTileanName(gender):
    if gender == 'male':
        first_name = random.choice(tilean_male_first_name)
    elif gender == 'female':
        first_name = random.choice(tilean_female_first_name)
    family_name = random.choice(tilean_family_name)
    final_name = first_name + " " + family_name
    return final_name

def retrieveDwarfName(gender):
    if gender == 'male':
        first_name = random.choice(dwarf_male_first_name)
    elif gender == 'female':
        first_name = random.choice(dwarf_female_first_name)
    family_name = random.choice(dwarf_family_names)
    clan_name = random.choice(dwarf_clan_names)
    final_name = first_name + " " + family_name + " of clan " + clan_name
    return final_name

def retrieveHalflingName(gender):
    if gender == 'male':
        first_name = random.choice(halfling_male_first_name)
    elif gender == 'female':
        first_name = random.choice(halfling_female_first_name)
    clan_name = random.choice(halfling_clan_names)
    final_name = first_name + " " + clan_name
    return final_name

def retrieveElfName(kind):
    firstName = ''
    firstComponent = random.choice(elf_first_component)
    middleComponents = random.sample(elf_second_component, 3)
    if kind == 'high':
        finalComponent = random.choice(high_elf_final_component)
        epithet = random.choice(high_elf_epithets)
    elif kind == 'wood':
        finalComponent = random.choice(wood_elf_final_component)
        epithet = random.choice(wood_elf_epithets)
    
    extraComponentChance = random.randint(1,12)
    if extraComponentChance <= 9:
        middleComponent = middleComponents[0]
    elif extraComponentChance <= 11:
        middleComponent = middleComponents[0] + middleComponents[1]
    elif extraComponentChance == 12:
        middleComponent = middleComponents[0] + middleComponents[1] + middleComponents[2]
    firstName += firstComponent + middleComponent + finalComponent
    firstName.replace('thth','th')
    finalName = firstName + " " + epithet
    return finalName

def retrieveHighElfName(gender):
    name = retrieveElfName('high')
    return name

def retrieveWoodElfName(gender):
    name = retrieveElfName('wood')
    return name

def retrieveCharacterName(species, gender):
    if species == 'human':
        name = retrieveReiklanderName(gender)
    elif species == 'dwarf':
        name = retrieveDwarfName(gender)
    elif species == 'halfling':
        name = retrieveHalflingName(gender)
    elif species == 'high elf':
        name = retrieveHighElfName(gender)
    elif species == 'wood elf':
        name = retrieveWoodElfName(gender)
    elif ' familiar' in species:        
        prevName = retrieveReiklanderName(gender).split()
        name = prevName[0]
    elif 'tilean human' in species:
        name = retrieveTileanName(gender)
    return name
