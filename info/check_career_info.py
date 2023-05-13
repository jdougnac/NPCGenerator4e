from career_info import *
import test
import pytest


def careerInfoContentIsCorrect():
    errors = []
    for career in career_list:
        specific_career_errors = [career_list[career]['name']]
        if len(career_list[career]['ranks']) != 4:
            specific_career_errors.append('wrong amount of ranks')
        if len(career_list[career]['status']) != 4:
            specific_career_errors.append('wrong amount of status')            
        if len(career_list[career]['stats']) != 4:
            specific_career_errors.append('wrong amount of stats')  
        if len(career_list[career]['stats'][0]) != 3:
            specific_career_errors.append('wrong amount of stats 0')  
        if len(career_list[career]['stats'][1]) != 1:
            specific_career_errors.append('wrong amount of stats 1')  
        if len(career_list[career]['stats'][2]) != 1:
            specific_career_errors.append('wrong amount of stats 2')  
        if len(career_list[career]['stats'][3]) != 1:
            specific_career_errors.append('wrong amount of stats 3')
        if len(career_list[career]['skills'][0]) != 8:
            specific_career_errors.append('wrong amount of skills 0')  
        if len(career_list[career]['skills'][1]) != 6:
            specific_career_errors.append('wrong amount of skills 1')  
        if len(career_list[career]['skills'][2]) != 4:
            specific_career_errors.append('wrong amount of skills 2')  
        if len(career_list[career]['skills'][3]) != 2:
            specific_career_errors.append('wrong amount of skills 3')        
        if len(career_list[career]['talents'][0]) != 4:
            specific_career_errors.append('wrong amount of talents 0')  
        if len(career_list[career]['talents'][1]) != 4:
            specific_career_errors.append('wrong amount of talents 1')  
        if len(career_list[career]['talents'][2]) != 4:
            specific_career_errors.append('wrong amount of talents 2')  
        if len(career_list[career]['talents'][3]) != 4:
            specific_career_errors.append('wrong amount of talents 3')        
        if career_list[career]['name'].lower() != career:
            specific_career_errors.append('name different from career')   
        if len(career_list[career]['trappings']) != 4:
            specific_career_errors.append('wrong amount of trappings')    
        errors.append(specific_career_errors)
    for item in errors:
        if len(item) != 1:
            print(item)
            

careerInfoContentIsCorrect()                                