import random, copy
from NPCGenerator4e.info import species_selection as ss
from NPCGenerator4e.info.talent_info import *
from NPCGenerator4e.info import career_info


def determineAnyTalent(talent):
    processed_talent = talent[:talent.index('(')-1]
    return processed_talent+' ('+random.choice(detailed_talents[processed_talent])+')'


def generateInitialSpeciesTalents(species):
    talentList = ss.final_species_dict[species]['talents']
    finalTalentList = []
    randomTalents = 0

    randomSpeciesTalents = random_species_talents[:]
    detailedTalents = copy.deepcopy(detailed_talents)
    for talent in talentList:
        if '%' in talent:
            newTalent = talent.split('%')
            talent = random.choice(newTalent)
        if '(any)' not in talent:
            finalTalentList.append(talent)
        else:
            newTalent = determineAnyTalent(talent)
            while newTalent in finalTalentList:
                newTalent = determineAnyTalent(talent)
            finalTalentList.append(newTalent)

    if species == 'halfling':
        randomTalents = 2
        detailedTalents['acute sense'].remove('taste')
        randomSpeciesTalents.remove('night vision')



    elif species == 'human' or ' human' in species:
        randomTalents = 3
        if 'savvy' in finalTalentList: 
            randomSpeciesTalents.remove('savvy')
        elif 'suave' in finalTalentList:
            randomSpeciesTalents.remove('suave')
    else:
        randomTalents = 0
    randomTalentList = random.sample(randomSpeciesTalents, randomTalents) #
    for talent in randomTalentList:
        if '(any)' in talent:
            newTalent = determineAnyTalent(talent) 
            while newTalent in finalTalentList:
                newTalent = determineAnyTalent(talent)
        else:
            newTalent = talent        
        finalTalentList.append(newTalent)

    return finalTalentList

def generateCareerTalent(speciesTalents, career):
    finalTalents = speciesTalents[:]
    talent = random.choice(career_info.final_career_list[career]['talents'][0])
    if '(any)' in talent:
        talent = determineAnyTalent(talent)  
        
    while talent in speciesTalents:
        talent = random.choice(career_info.final_career_list[career]['talents'][0])
        if '(any)' in talent:
            talent = determineAnyTalent(talent) 
    finalTalents.append(talent)
    return finalTalents

