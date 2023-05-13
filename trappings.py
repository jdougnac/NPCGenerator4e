import random
from NPCGenerator4e.info import career_info


def getRandomAmountTrapping(trapping):
    trapping = trapping.split('|')
    amount = trapping[0].split('°')
    finalAmount = random.randint(int(amount[0]),int(amount[1]))
    finalTrapping = str(finalAmount) +" "+ trapping[1]
    return finalTrapping

def getCareerTrappings(career,level):
    trappingsList = []
    for x in range(0,int(float(level))):
        for item in career_info.final_career_list[career]['trappings'][x]:
            if '|' in item:
                trappingsList.append(getRandomAmountTrapping(item))
            elif '%' in item:
                temp = item.split('%')
                trappingsList.append(random.choice(temp))                
            else:
                trappingsList.append(item)
    return trappingsList
    
def getClassTrappings(NPCclass):
    trappings = []
    if NPCclass != 'special':
        for trapping in career_info.class_trappings[NPCclass]:
            if '°' in trapping:
                trappings.append(getRandomAmountTrapping(trapping))
            elif '%' in trapping:
                temp = trapping.split('%')
                trappings.append(random.choice(temp))
            else:
                trappings.append(trapping)
    return trappings


def getCareerWealth(career, level):
    brass = 0
    silver = 0
    gold = 0
    finalBrass = 0
    finalSilver = 0
    initial = career_info.final_career_list[career]['status']
    finalWealth = []
 
    
    divided = initial[int(float(level))-1].split()
    if divided[0] == 'brass':
        brass += int(divided[1])
    elif divided[0] == 'silver':
        silver += int(divided[1])
    elif divided[0] == 'gold':
        gold += int(divided[1]) 
                    
    for coin in range(0,brass):
        finalBrass += random.randint(1,10) + random.randint(1,10)
    for coin in range(0,silver):
        finalSilver += random.randint(1,10)
    if finalBrass != 0:
        finalWealth.append(str(finalBrass)+' pennies')
    if finalSilver == 1:
        finalWealth.append('1 shilling')
    elif finalSilver >1:
        finalWealth.append(str(finalSilver)+' shillings')
    if gold == 1:
        finalWealth.append('1 crown')
    elif gold >1:
        finalWealth.append(str(gold)+' crowns')
    return finalWealth