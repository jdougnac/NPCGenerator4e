import random

def return_stats(career_group, species):



    species_stats = species
    if career_group == 'academic':
        first_stat =7
        second_stat =8

    elif career_group == 'burgher':
        first_stat =7
        second_stat =9

    elif career_group == 'courtier':
        first_stat =9
        second_stat =8
    elif career_group == 'peasant':
        first_stat =3
        second_stat =2
    elif career_group == 'ranger':
        first_stat =5
        second_stat =3
    elif career_group == 'riverfolk':
        first_stat =5
        second_stat =6
    elif career_group == 'rogue':
        first_stat =6
        second_stat =5
    elif career_group == 'warrior':
        first_stat =0
        second_stat =1
           

    added_numbers =[]
    raw_stats = [0,0,0,0,0,0,0,0,0,0]
    for x in range(0,10):
        added_numbers.append(random.randint(1,10)+random.randint(1,10))
    
    raw_stats[first_stat] = max(added_numbers)
    added_numbers.remove(max(added_numbers))

    raw_stats[second_stat] = max(added_numbers)
    added_numbers.remove(max(added_numbers))

    
    for x in range(0,len(raw_stats)):
        if raw_stats[x] == 0:
            raw_stats[x] = added_numbers[0]
            del added_numbers[0]
    

    final_stats = []
    
    for x in range(0,len(raw_stats)):
        final_stats.append(species_stats[x]+raw_stats[x])

    while species[12] > 0:
        number = random.randint(0,1)
        if number == 0:
            species[10]+=1
        else:
            species[11]+=1
        species[12]-=1

    final_stats.append(species[10])
    final_stats.append(species[11])
    final_stats.append(species[12])
    final_stats.append(species[13])
    
    

    return final_stats



