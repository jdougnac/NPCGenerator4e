
import random
careers = {
'academic' : ['apothecary','engineer','lawyer','nun','physician','priest','scholar','wizard'],
'burgher':['agitator','artisan','beggar','investigator','merchant','rat catcher','townsman','watchman'],
'courtier':['advisor','artist','duellist','envoy','noble','servant','spy','warden'],
'peasant':['bailiff','hedge witch','herbalist','hunter','miner','mystic','scout','villager'],
'ranger':['bounty hunter','coachman','entertainer','flagellant','messenger','pedlar','road warden','witch hunter'],
'riverfolk':['boatman','huffer','riverwarden','riverwoman','seaman','smuggler','stevedore','wrecker'],
'rogue':['bawd','charlatan','fence','grave robber','outlaw','racketeer','thief','witch'],
'warrior': ['cavalryman','guard','knight','pit fighter','protagonist','soldier','slayer','warrior priest']
}

exclusive_careers = {
    'dwarf': {'warrior':['slayer']},
    'human': {'academic': ['alchemist','astromancer','druid','hierophant','magister vigilant','nun','priest','shadowmancer','shaman','spiriter'],
              'peasant': ['hedge witch','scryer'],
              'ranger': ['flagellant','witch hunter'],
              'rogue': ['witch'],
              'warrior': ['warrior priest']}
}

forbidden_careers = {
    'dwarf': {'academic': ['alchemist','astromancer','druid','hierophant','magister vigilant',
                           'nun','priest','pyromancer','shadowmancer','shaman','spiriter','wizard'],
              'peasant': ['hedge witch','herbalist','mystic','scryer'],
              'ranger': ['flagellant','road warden', 'witch hunter'],
              'riverfolk': ['riverwarden'],
              'rogue': ['bawd','charlatan','grave robber','witch'],
              'warrior': ['cavalryman','knight','warrior priest']},

    'halfling': {'academic': ['alchemist','astromancer','druid','hierophant','magister vigilant',
                              'nun','priest','pyromancer','shadowmancer','shaman','spiriter','wizard'],
                 'courtier': ['duellist','noble'],
                 'peasant': ['hedge witch','mystic','scryer'],
                 'ranger': ['flagellant','witch hunter'],
                 'riverfolk': ['wrecker'],
                 'rogue': ['witch'],
                 'warrior': ['cavalryman','knight','protagonist','slayer','warrior priest']},

    'high elf': {'academic': ['alchemist','astromancer','druid','engineer','hierophant','magister vigilant',
                              'mundane alchemist','nun','priest','pyromancer','shadowmancer','shaman','spiriter'],
                 'burgher': ['agitator','beggar','rat catcher'],
                 'courtier': ['servant'],
                 'peasant':['bailiff','hedge witch','miner','mystic','scryer','villager'],
                 'ranger': ['coachman','flagellant','pedlar','road warden','witch hunter'],
                 'riverfolk': ['huffer','riverwarden','riverwoman','stevedore','wrecker'],
                 'rogue': ['fence','grave robber','racketeer','thief', 'witch'],
                 'warrior':['beadle','slayer','warrior priest']},

    'human': {'warrior':['slayer']},


    'wood elf': {'academic':['alchemist','apothecary','astromancer','druid','engineer','hierophant','lawyer',
                             'magister vigilant','mundane alchemist','nun','priest','physician','pyromancer','shadowmancer','shaman','spiriter'],
                 'burgher':['agitator','beggar','investigator', 'merchant','rat catcher','townsman','watchman'],
                 'courtier': ['duellist','servant','warden'],
                 'peasant': ['bailiff','hedge witch','miner','scryer','villager'],
                 'ranger': ['coachman','flagellant','pedlar','road warden','witch hunter'],
                 'riverfolk': ['boatman','huffer','riverwarden','riverwoman','seaman','smuggler','stevedore'],
                 'rogue': ['bawd', 'charlatan','fence','grave robber','racketeer','thief', 'witch'],
                 'warrior': ['beadle','protagonist', 'slayer', 'warrior priest']
        }
}

special_species = {
    'combat familiar': ['combat familiar'],
    'spell familiar': ['spell familiar']
}

