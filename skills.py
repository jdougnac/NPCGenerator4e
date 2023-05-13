from NPCGenerator4e.info import detailed_skills as ds
from NPCGenerator4e.info import species_selection as ss
from NPCGenerator4e.info.detailed_skills import *
from NPCGenerator4e.info import career_info
import random

def selectAnySkill(skill):
    processed_skill = skill[:skill.index('(')-1]
    return processed_skill+' ('+random.choice(any_skills[processed_skill])+')'

def retrieveSpeciesSkillList(species):
    skillList = []
    anySkillList = []
    
    for skill in ss.final_species_dict[species]['skills']:
        if '(any)' in skill:
            anySkillList.append(skill)
        else:
            skillList.append(skill)
    for skill in anySkillList:
        final_skill = selectAnySkill(skill)
        skillList.append(final_skill)
    return skillList
      
def initialAdvanceSpeciesSkills(skillList):
    skillDictionary = {}
    advance = random.sample(skillList,6)
    for item in skillList:
        if item not in advance:
            skillDictionary[item] = 0
    skillDictionary[advance[0]] = 5
    skillDictionary[advance[1]] = 5
    skillDictionary[advance[2]] = 5
    skillDictionary[advance[3]] = 3
    skillDictionary[advance[4]] = 3
    skillDictionary[advance[5]] = 3
    return skillDictionary

def retrieveCareerInitialSkillList(career):
    skillList = []
    anySkillList = []
    for skill in career_info.final_career_list[career]['skills'][0]:
        if '(any)' in skill:
            anySkillList.append(skill)
        elif '%' in skill:
            skills = skill.split('%')
            chosenSkillPosition = random.randint(0,1)
            if skills[chosenSkillPosition] not in skillList:
                skillList.append(skills[chosenSkillPosition])
            else:
                del skills[chosenSkillPosition]
                skillList.append(skills[0])
        else:
            skillList.append(skill)
    for skill in anySkillList:
        final_skill = selectAnySkill(skill)
        skillList.append(final_skill)
    return skillList

def initialAdvanceCareerSkills(skillList):
    skillPointsAssigned = 0
    skillDict = {}
    for item in skillList:
        skillDict[item] = 0
    while skillPointsAssigned < 40:
        skill = random.choice(skillList)
        if skillDict[skill] < 10:
            skillDict[skill] +=1
            skillPointsAssigned +=1
    return skillDict

def combineInitialSkills(initial_species_skills, initial_career_skills):
    species_skills = initial_species_skills
    career_skills = initial_career_skills
    to_delete = []
    final_skill_list = []
    for x in species_skills:
        if x in career_skills:
            career_skills[x] += species_skills[x]
            to_delete.append(x)
    for y in to_delete:
        del species_skills[y]
    final_skill_list.append(species_skills)
    final_skill_list.append(career_skills)
    return final_skill_list








