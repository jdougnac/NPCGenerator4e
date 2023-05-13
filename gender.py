import random

def assignGender(gender):
    if gender == 'female':
        return 'female'
    elif gender == 'male':
        return 'male'
    else:
        return random.choice(['male','female'])