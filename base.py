import random
import copy
from NPCGenerator4e.info import career_info, spells, talent_info, career_selection, species_selection, detailed_skills, extra_books

from .gender import *
from .attributes import *
from .career import *
from .skills import *
from .names import *
from .finalDetails import *
from .species import *
from .talents import *
from .trappings import *




def advanceStats(stats, level):
    attributeAdvances = [0,0,0,0,0,0,0,0,0,0]
    for attribute in stats[0]:
        attributeAdvances[attribute] = int(float(level)) *5
    for attribute in range(1,int(float(level))):
        attributeAdvances[stats[attribute][0]] = int(float(level)) *5    
    return attributeAdvances

def addTalents(currentTalents, careerTalents, level):
    for talent in careerTalents[0]:
        if talent not in currentTalents:
            if '(any)' in talent:
                talent = determineAnyTalent(talent)
            currentTalents.append(talent)  
    for level in range(1,int(float(level))):        
        for talent in careerTalents[level]:
            if '(any)' in talent:                
                talent = determineAnyTalent(talent)
            elif '%' in talent:
                talents = talent.split('%')
                chosenTalentPosition = random.randint(0,len(talents))
                if talents[chosenTalentPosition] not in currentTalents:
                   talent = talents[chosenTalentPosition]
            currentTalents.append(talent)
    return currentTalents

def advanceSkills(currentSkillList,careerSkillList,level):
    currentSkills = currentSkillList[:]
    careerSkills = copy.deepcopy(careerSkillList)
    for careerLevel in range(0, len(careerSkills)):
        for skill in careerSkills[careerLevel]:
            if '%' in skill:    
                new_skill = random.choice(skill.split('%'))
                careerSkills[careerLevel].append(new_skill)
                careerSkills[careerLevel].remove(skill)
    for careerLevel in range(1,int(float(level))):
        for skill in careerSkills[careerLevel]:
            currentSkills[1][skill] = 0
        skill_list = list(currentSkills[1].keys())        
        for skill in range(0,len(skill_list)):         
            if '(any)' in skill_list[skill]:
                del currentSkills[1][skill_list[skill]]
                skill_list[skill] = selectAnySkill(skill_list[skill]) 
        skills_to_advance = random.sample(skill_list, 8)
        for skill_adv in skills_to_advance:
            currentSkills[1][skill_adv] = (careerLevel+1)*5
    
    speciesSkillAdvances = (int(float(level)))*5
    
    speciesSkillList =list(currentSkills[0].keys())
    for advance in range(0, speciesSkillAdvances):
        skillToAdvance = random.choice(speciesSkillList)
        currentSkills[0][skillToAdvance] += 1
    return currentSkills

def advanceCharacter(character):

    career = career_info.final_career_list[character['career']]
    character['attributeAdvances'] = advanceStats(career['stats'], character['level'])
    

    if character['level'] == '1':
        return character 
    if character['level'] == '1.5':
        character['level'] = '1' 

    character['careerTalents'] = addTalents(character['careerTalents'],career['talents'], character['level'])

    character['skills'] = advanceSkills(character['skills'], career['skills'], character['level'])



    return character

def deleteRepeatSkills(skills):
    for skill in list(skills[0]):
        if skill in skills[1]:
            del skills[0][skill]
    return skills

def setPettyMagicSpells(willpower):
        
    wp = willpower   
    pettyMagicSpells = random.sample(spells.final_arcane_spells['petty'], int(wp))
    pettyMagicSpells.sort()
    return pettyMagicSpells

def checkForSpells(talentList, skillList, characterLevel):
    blessCount = 0

    windSpells = []
    miracles = []
    blessings = []
    isSuffused = False
    for talent in talentList:
        if 'suffuse with (' in talent:
           
            isSuffused = True
            position = talentList.index(talent)
        if 'arcane magic (' in talent:
           
            place = talentList.index(talent)
            for skill in skillList[1]:
                if 'channeling (' in skill:
                    channel = skill[12:-1]                    
            first = talent.find('(')
            talent = talent[:first+1]+channel+')'            
            wind = talent[talent.find('(')+1:-1]
            if isSuffused == True:
                suffusePos = talent.find('(')
                arcaneWind = talent[14:-1]
                talentList[position] = talentList[position][:suffusePos+1]+arcaneWind+')' 

            
            spellList = []
            for spell in spells.final_arcane_spells['arcane']:
                spellList.append(spell)
            for spell in spells.final_arcane_spells['winds'][wind]:
                spellList.append(spell) 
            windSpells = random.sample(spellList, int(float(characterLevel)))
            talentList[place] = talent
            windSpells.sort()

        
        if 'bless (' in talent:
            blessCount +=1
            blessings = spells.blessings[talent[7:-1]]
            blessings.sort()
        
        if 'invoke (' in talent:            
            place = talentList.index(talent)
            for findTalent in talentList:
                if 'bless (' in findTalent:
                    channel = findTalent[7:-1]                    
            first = talent.find('(')
            talent = talent[:first+1]+channel+')'
            hasInvoke = True

            
            deity = talent[talent.find('(')+1:-1]

            miracles = random.sample(spells.miracles[deity], int(float(characterLevel)))
            talentList[place] = talent
            miracles.sort()
    if blessCount == 2:
        for talent in talentList:
            if 'bless (' in talent:
                erase = talent[:]
                break
        talentList.remove(erase)

   
    if len(miracles)  != 0:
        returnedList = ['miracles',True,miracles,blessings]
    elif len(blessings) != 0:
        returnedList = ['blessings',False,blessings]
    elif len(windSpells) != 0:
        returnedList = ['windSpells',True, windSpells]
    else:
        returnedList = ['',False]
    return returnedList
    
def addSkillCharacteristic(skillList, baseChars, charAdvances):
    finalSkillList = []
    for skill in skillList:
        finalSkill = [skill[0],skill[1]]
        if '(' in finalSkill[0]:
            position = finalSkill[0].find('(')-1
            skillName =finalSkill[0][0:position]
        else:
            skillName = finalSkill[0]
        finalSkill.append(skill_chars[skillName])

        if finalSkill[2] == 'WS':
            statPosition = 0
        elif finalSkill[2] == 'BS':
            statPosition = 1
        elif finalSkill[2] == 'S':
            statPosition = 2
        elif finalSkill[2] == 'T':
            statPosition = 3
        elif finalSkill[2] == 'I':
            statPosition = 4
        elif finalSkill[2] == 'Ag':
            statPosition = 5
        elif finalSkill[2] == 'Dex':
            statPosition = 6
        elif finalSkill[2] == 'Int':
            statPosition = 7
        elif finalSkill[2] == 'WP':
            statPosition = 8
        elif finalSkill[2] == 'Fel':
            statPosition = 9
        finalSkill.append(baseChars[statPosition] + charAdvances[statPosition])
        finalSkill.append(finalSkill[1] + finalSkill[3])
        finalSkillList.append(finalSkill)        
    return finalSkillList

def elementsFromOtherBooks(books, career, species):
    extraCareers = []    
    for book in extra_books.additional_books:
        for newCareer in extra_books.additional_books[book]['careers']:
            extraCareers.append(newCareer)
        for newSpecies in extra_books.additional_books[book]['species']:
            if species == newSpecies:
                species_selection.final_species_dict[species] = extra_books.additional_books[book]['species'][species]
    if species in career_selection.special_species:
        career = random.choice(career_selection.special_species[species])
        for book in extra_books.additional_books:#
            for newCareer in extra_books.additional_books[book]['careers']:#
                extraCareers.append(newCareer)#
    if career in extraCareers: #
        for extraCareer in extraCareers:
            career_info.final_career_list[extraCareer] = career_info.extra_careers[extraCareer] #cambiar por career en caso de bug


    for book in books:        
        for career in extra_books.additional_books[book]['careers']:
            selectedCareer = career_info.extra_careers[career]
            career_info.final_career_list[career] = selectedCareer
            if selectedCareer['class'] != 'Special':   
                career_selection.careers[selectedCareer['class'].lower()].append(career)                
        for wind in extra_books.additional_books[book]['spells']['winds']:
            for spell in extra_books.additional_books[book]['spells']['winds'][wind]:
                spells.final_arcane_spells['winds'][wind].append(spell)
        for species in extra_books.additional_books[book]['species']:
            species_selection.final_species_dict[species] = extra_books.additional_books[book]['species'][species]
            if ' human' in species:
                career_selection.forbidden_careers[species] = career_selection.forbidden_careers['human']
        
   

def createCharacter(charGender, charSpecies, gameClass, charCareer, charLevel, books):
    spells.final_arcane_spells = copy.deepcopy(spells.arcane_spells)
    species_selection.final_species_dict = copy.deepcopy(species_selection.species_dict)
    career_info.final_career_list = copy.deepcopy(career_info.career_list)
    career_selection_list = copy.deepcopy(career_selection.careers)
    elementsFromOtherBooks(books,charCareer, charSpecies)
    character = {}

    if charLevel == 'random':
        characterLevel = random.choice([1,1,1,1,1,2,2,2,3,3,4])
    else:
        characterLevel = charLevel
    
    character['level'] = characterLevel

    if charSpecies == 'random':
        forceSpecies = False
    else:
        forceSpecies = True

    characterGender = assignGender(charGender)
    characterSpecies = assignSpecies(charSpecies)
    characterCareer = pickCareer(characterSpecies, gameClass, charCareer)

    if forceSpecies == False and characterSpecies not in career_selection.special_species:
        while forceSpecies == False:
            isCareerForbidden = False        
            for path in career_selection.forbidden_careers[characterSpecies]:
                if characterCareer in career_selection.forbidden_careers[characterSpecies][path]:
                    
                    isCareerForbidden = True                
                    
            if isCareerForbidden == True:                
                characterSpecies = random.choice(list(species_selection.final_species_dict.keys()))
            elif isCareerForbidden == False:
                forceSpecies = True

    character['gender'] = characterGender
    character['species'] = characterSpecies
    character['career'] = characterCareer    
    #character['careerPath'] = career_selection_list[characterCareer]['name']
    character['careerPath'] = career_info.final_career_list[character['career']]['name'] #
    character['careerClass'] = career_info.final_career_list[characterCareer]['class'] #
    character['status'] = career_info.final_career_list[characterCareer]['status'][int(float(characterLevel))-1] #
    character['careerName'] = career_info.final_career_list[characterCareer]['ranks'][int(float(characterLevel))-1] #

    characterName = retrieveCharacterName(characterSpecies, characterGender)
    characterAge = retrieveAge(characterSpecies)
    characterEyeColour = retrieveEyeColour(characterSpecies)
    characterHairColour = retrieveHairColour(characterSpecies)
    characterHeight = retrieveHeight(characterSpecies)

    character['name'] = characterName
    character['age'] = characterAge
    character['eyeColour'] = characterEyeColour
    character['hairColour'] = characterHairColour
    character['height'] = characterHeight

    characterAttributes = generateStartingAttributes(characterSpecies)
    characterMovement = generateMovement(characterSpecies)
    characterFate = generateFate(characterSpecies)

    character['attributes'] = characterAttributes
    character['movement'] = characterMovement
    character['walkMovement'] = characterMovement *2
    character['runMovement'] = characterMovement *4
    character['fate'] = characterFate[0]
    character['resilience'] = characterFate[1]

    #

    characterInitialSpeciesSkills = retrieveSpeciesSkillList(characterSpecies)
    characterInitialCareerSkills = retrieveCareerInitialSkillList(characterCareer)
    
    characterSpeciesSkills = initialAdvanceSpeciesSkills(characterInitialSpeciesSkills)    
    characterCareerSkills = initialAdvanceCareerSkills(characterInitialCareerSkills)
    characterSkills = combineInitialSkills(characterSpeciesSkills, characterCareerSkills)

    character['skills'] = characterSkills

    characterSpeciesTalents = generateInitialSpeciesTalents(characterSpecies)
    characterCareerTalents = generateCareerTalent(characterSpeciesTalents, characterCareer)

    character['speciesTalents'] = characterSpeciesTalents
    
    character['careerTalents'] = characterCareerTalents

    characterWealth = getCareerWealth(characterCareer, characterLevel)
    characterClassTrappings = getClassTrappings(career_info.final_career_list[characterCareer]['class'].lower())
    characterCareerTrappings = getCareerTrappings(characterCareer, characterLevel)

    character['wealth'] = characterWealth
    character['classTrappings'] = characterClassTrappings
    character['careerTrappings'] = characterCareerTrappings

    character = advanceCharacter(character)

    notRepeatedSkills = deleteRepeatSkills(character['skills'])
    character['skills'] = notRepeatedSkills
    character['wounds'] = generateWounds(character['species'], (character['attributeAdvances'][2]+character['attributes'][2]),character['attributeAdvances'][3]+character['attributes'][3],character['attributeAdvances'][8]+character['attributes'][8])
 
    if 'petty magic' in character['careerTalents']:
        pettyMagicSpells = setPettyMagicSpells((character['attributes'][8] + character['attributeAdvances'][8])//10)
        character['pettyMagicSpells'] = pettyMagicSpells        


    spellCheck = checkForSpells(character['careerTalents'], character['skills'], character['level'])
    if spellCheck[0] == '' or spellCheck[0] == 'blessings':
        character['isCaster'] = False
    else:
        character['isCaster'] = True
    if spellCheck[0] == 'blessings':
        character['blessings'] = spellCheck[2]
    elif spellCheck[0] == 'miracles':
        character['miracles'] = spellCheck[2]  
        character['blessings'] = spellCheck[3]    
    elif spellCheck[0] == 'windSpells':
        character['windSpells'] = spellCheck[2]                    
    extraTalents = []

    if character['isCaster'] == False:
        while len(extraTalents) < int(float(character['level'])):
            talent = random.choice(character['careerTalents'])          
            if talent in repurchasable_talents and talent not in extraTalents and '(' not in talent:
                extraTalents.append(talent)

    character['extraTalents'] = extraTalents 
    for talent in character['extraTalents']:
        character['careerTalents'].append(talent)
            
    finalSkills = []

    for talent in character['careerTalents']:
        if talent == 'coolheaded':
            character['attributes'][8] += 5 
        elif talent == 'fleet footed':
            character['movement'] += 1
            character['walkMovement'] += 2 
            character['runMovement'] += 4 
        elif talent == 'lightning reflexes':
            character['attributes'][5] += 5             
        elif talent == 'marksman':
            character['attributes'][1] += 5             
        elif talent == 'nimble fingered':
            character['attributes'][6] += 5             
        elif talent == 'savvy':
            character['attributes'][7] += 5             
        elif talent == 'sharp':
            character['attributes'][4] += 5             
        elif talent == 'suave':
            character['attributes'][9] += 5             
        elif talent == 'very resilient':
            character['attributes'][3] += 5             
        elif talent == 'very strong':
            character['attributes'][2] += 5             
        elif talent == 'warrior born':
            character['attributes'][0] += 5   
        


    for skillList in list(character['skills'][0].items()), list(character['skills'][1].items()):
        for skill in skillList:
            finalSkills.append(skill)
    finalSkills.sort()

    finalSkillsDefinitiveEdition = addSkillCharacteristic(finalSkills, character['attributes'],character['attributeAdvances'] )
    
    character['careerTalents'].sort()

    character['finalTalents'] = character['careerTalents']
    character['finalSkills'] = finalSkillsDefinitiveEdition

    career_selection.careers = career_selection_list

    return character





