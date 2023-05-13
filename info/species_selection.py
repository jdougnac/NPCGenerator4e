
species_dict = {
'dwarf' : {'name': 'dwarf',
           'stats' : [30,20,20,30,20,10,30,20,40,10,0,2,2,3],
           'skills': ['consume alcohol', 'cool', 'endurance', 'entertain (storytelling)', 'evaluate', 'intimidate',
                      'language (khazalid)', 'lore (dwarfs)', 'lore (geology)', 'lore (metallurgy)', 'melee (basic)',
                      'trade (any)'],
           'talents': ['magic resistance', 'night vision', 'read/write%relentless','resolute%strong-minded','sturdy']
           },

'halfling' : {'name': 'halfling',
           'stats' : [10,30,10,20,20,20,30,20,30,30,0,2,3,3],
           'skills': ['charm','consume alcohol','dodge','gamble','haggle','intuition', 'language (mootish)',
           'lore (reikland)', 'perception', 'sleight of hand','stealth (any)', 'trade (cook)'],
           'talents': ['acute sense (taste)','night vision', 'resistance (chaos)', 'small']
           },

'human' : {'name': 'human',
           'stats' : [20,20,20,20,20,20,20,20,20,20,2,1,3,4],
           'skills': ['animal care','charm','cool','evaluate','gossip','haggle','language (bretonnian)','language (wastelands)',
           'leadership', 'lore (reikland)','melee (basic)', 'ranged (bow)'],
           'talents': ['doomed','savvy%suave']
           },

'high elf' : {'name': 'high elf',
           'stats' : [30,30,20,20,40,30,30,30,30,20,0,0,2,5],
           'skills': ['cool','entertain (singing)','evaluate','language (eltharin)','leadership', 'melee (basic)', 'navigation','perception', 'play (any)', 'ranged (bow)', 'sail', 'swim'],
           'talents': ['acute sense (sight)', 'coolheaded%savvy','night vision','second sight%sixth sense', 'read/write']
           },

'wood elf' : {'name': 'wood elf',
           'stats' : [30,30,20,20,40,30,30,30,30,20,0,0,2,5],
           'skills': ['athletics','climb','endurance','entertain (singing)','intimidate', 'language (eltharin)','melee (basic)',
           'outdoor survival','perception','ranged (bow)', 'stealth (rural)','track'],
           'talents': ['acute sense (sight)','hardy%second sight','night vision','read/write%very resilient','rover']
           }
            }

final_species_dict = {}