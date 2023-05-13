

career_list = {

    'apothecary': {
        'ranks': ["Apothecary Apprentice", 'Apothecary', 'Master Apothecary', 'Apothecary-General'],
        'status': ['brass 3', 'silver 1', 'silver 3', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 6, 7], [9], [4], [8]],
        'skills': [['consume alcohol', 'heal', 'language (classical)', 'lore (chemistry)',
                    'lore (medicine)', 'lore (plants)', 'trade (apothecary)', 'trade (poisoner)'],
                   ['charm', 'haggle',
                       'lore (science)', 'gossip', 'language (guilder)', 'perception'],
                   ['intuition', 'leadership', 'research',
                       'secret signs (guilder)'],
                   ['intimidate', 'ride (horse)']
                   ],
        'talents': [
            ['concoct', 'craftsman (apothecary)',
             'etiquette (scholar)', 'read/write'],
            ['criminal', 'dealmaker', 'etiquette (guilder)', 'pharmacist'],
            ['bookish', 'master tradesman (apothecary)',
             'resistance (poison)', 'savvy'],
            ['acute sense (taste)', 'coolheaded',
             'master tradesman (poisoner)', 'savant (apothecary)']
        ],
        'name': 'Apothecary',
        'class': 'Academic',
        'trappings': [
            ['book (blank)', 'healing draught',
             'leather jerkin', 'pestle and mortar'],
            ['guild licence', 'trade tools'],
            ['book (apothecary)', 'apprentice', 'workshop'],
            ['commission papers', 'large workshop']]
    },

    ###


    'engineer': {
        'ranks': ['Student Engineer', 'Engineer', 'Master Engineer', 'Chartered Engineer'],
        'status': ['brass 4', 'silver 2', 'silver 4', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[1, 6, 7], [4], [3], [8]],
        'skills': [
            ['consume alcohol', 'cool', 'endurance',
                'language (classical)', 'lore (engineer)', 'perception', 'ranged (blackpowder)', 'trade (engineer)'],
            ['drive', 'dodge', 'navigation',
                'ranged (engineering)', 'research', 'language (guilder)'],
            ['language (khazalid)', 'leadership', 'ride (horse)',
             'secret signs (guilder)'],
            ['language (any)', 'lore (any)']
        ],
        'talents':
        [
            ['artistic', 'gunner', 'read/write', 'tinker'],
            ['craftsman (engineer)', 'etiquette (guilder)',
             'marksman', 'orientation'],
            ['etiquette (scholar)', 'master tradesman (engineering)',
             'sniper', 'super numerate'],
            ['magnum opus', 'rapid reload',
                'savant (engineering)', ' unshakeable']
        ],
        'name': 'Engineer',
        'class': 'Academic',
        'trappings': [
            ['book (engineer)', 'hammer and spikes'],
            ['guild licence', 'trade tools'],
            ['workshop'],
            ['guild license',
                'library (engineer)', 'quality trade tools (engineer)', 'large workshop (engineer)']
        ]
    },

    ###

    'lawyer': {
        'ranks': ['Student Lawyer', 'Lawyer', 'Barrister', 'Judge'],
        'status': ['brass 4', 'silver 3', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[4, 6, 7], [9], [8], [3]],
        'skills': [
            ['consume alcohol', 'endurance', 'haggle',
                'language (classical)', 'lore (law)', 'lore (theology)', 'perception', 'research'],
            ['bribery', 'charm', 'gossip', 'intuition',
                'language (guilder)', 'secret signs (guilder)'],
            ['art (writing)', 'entertain (speeches)',
             'intimidate', 'lore (any)'],
            ['cool', 'lore (any)']
        ],
        'talents':
        [
            ['blather', 'etiquette (scholar)', 'read/write', 'speedreader'],
            ['argumentative', 'criminal', 'etiquette (guilder)', 'suave'],
            ['bookish', 'cat-tongued', 'impassioned zeal', 'savvy'],
            ['commanding presence', 'kingpin', 'savant (law)', 'wealthy']
        ],
        'name': 'Lawyer',
        'class': 'Academic',
        'trappings': [
            ['book (law)', 'magnifying glass'],
            ['court robes', 'guild licence', 'writing kit'],
            ['office', 'assistant'],
            ['gavel', 'ostentatious wig']
        ]
    },

    ###

    'nun': {
        'ranks': ['Novitiate', 'Nun', 'Abbess', 'Prioress General'],
        'status': ['brass 1', 'brass 4', 'silver 2', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[6, 7, 9], [8], [4], [3]],
        'skills': [
            ['art (calligraphy)', 'cool', 'endurance', 'entertain (storyteller)',
             'gossip', 'heal', 'lore (theology)', 'pray'],
            ['charm', 'melee (any)', 'research', 'trade (brewer)',
             'trade (herbalist)', 'trade (vintner)'],
            ['leadership', 'lore (local)', 'lore (politics)', 'perception'],
            ['language (any)', 'lore (any)']
        ],
        'talents':
        [
            ['bless (any)', 'stone soup', 'panhandle', 'read/write'],
            ['etiquette (cultists)', 'field dressing',
             'holy visions', 'invoke (any)'],
            ['resistance (any)', 'robust', 'savant (theology)',
             'stout-hearted'],
            ['commanding presence', 'iron will', 'pure soul', 'strong-minded']
        ],
        'name': 'Nun',
        'class': 'Academic',
        'trappings': [
            ['religious symbol', 'robes'],
            ['book (religion)', 'religious relic', ' trade tools (any)'],
            ['abbey', 'library (theology)'],
            ['religious order']]
    },

    ###

    'physician': {
        'ranks': ["Physician apprentice", 'Physician', 'Doktor', 'Court Physician'],
        'status': ['brass 4', 'silver 3', 'silver 5', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[6, 7, 8], [9], [4], [5]],
        'skills': [
            ['bribery', 'cool', 'drive', 'endurance', 'gossip',
                'heal', 'perception', 'sleight of hand'],
            ['charm', 'haggle', 'language (guilder)', 'lore (anatomy)',
             'lore (medicine)', 'trade (barber)'],
            ['consume alcohol', 'intimidate', 'leadership', 'research'],
            ['lore (noble)', 'perform (dancing)']
        ],
        'talents':
        [
            ['bookish', 'field dressing', 'read/write', 'strike to stun'],
            ['coolheaded', 'criminal', 'etiquette (guilder)', 'surgery'],
            ['etiquette (scholars)', 'resistance (disease)',
             'savvy', 'strike to injure'],
            ['etiquette (nobles)', 'nimble fingered',
             'savant (medicine)', 'strong-minded']
        ],
        'name': 'Physician',
        'class': 'Academic',
        'trappings': [
            ['bandages', 'healing draught'],
            ['book (medicine)', 'guild licence', 'trade tools (medicine)'],
            ['apprentice', 'workshop (medicine)'],
            ['courtly attire', 'letter of appointment']
        ]
    },

    ###

    'priest': {
        'ranks': ['Initiate', 'Priest', 'High Priest', 'Lector'],
        'status': ['brass 2', 'silver 1', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 5, 8], [9], [7], [4]],
        'skills': [
            ['athletics', 'cool', 'endurance', 'intuition',
                'lore (theology)', 'perception', 'pray', 'research'],
            ['charm', 'entertain (storytelling)', 'gossip',
             'heal', 'intimidate', 'melee (basic)'],
            ['art (writing)', 'entertain (speeches)',
             'leadership', 'lore (heraldry)'],
            ['language (any)', 'lore (politics)']
        ],
        'talents':
        [
            ['bless (any)', 'holy visions', 'read/write', 'suave'],
            ['blather', 'bookish', 'etiquette (cultists)', 'invoke (any)'],
            ['acute sense (any)', 'hatred (any)',
             'impassioned zeal', 'strong-minded'],
            ['master orator', 'pure soul',
                'resistance (any)', 'savant (theology)']
        ],
        'name': 'Priest',
        'class': 'Academic',
        'trappings': [
            ['religious symbol', 'robes'],
            ['book (religion)', 'ceremonial robes'],
            ['quality robes', 'religious relic', 'subordinate priests', 'temple'],
            ['library (theology)', 'subordinate high priests']
        ]
    },

    ###

    'scholar': {
        'ranks': ['student', 'scholar', 'fellow', 'professor'],
        'status': ['brass 3', 'silver 2', 'silver 5', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 7, 8], [4], [9], [6]],
        'skills': [
            ['consume alcohol', 'entertain (storytelling)', 'gamble', 'gossip',
             'haggle', 'language (classical)', 'lore (any)', 'research'],
            ['art (writing)', 'intuition', 'language (any)',
             'lore (any)', 'perception', 'trade (any)'],
            ['entertain (lecture)', 'intimidate',
             'language (any)', 'lore (any)'],
            ['entertain (rhetoric)', 'lore (any)']
        ],
        'talents':
        [
            ['carouser', 'read/write', 'savvy', 'super numerate'],
            ['bookish', 'etiquette (scholars)', 'speedreader', 'suave'],
            ['linguistics', 'public speaker',
                'savant (any)', 'tower of memories'],
            ['magnum opus', 'master orator', 'savant (any)', 'sharp']
        ],
        'name': 'Scholar',
        'class': 'Academic',
        'trappings': [
            ['alcohol', 'book', 'opinions', 'writing kit'],
            ['access to a library', 'degree'],
            ['mortarboard', 'robes'],
            ['study']
        ]
    },

    ###

    'wizard': {
        'ranks': ["Wizard Apprentice", 'Wizard', 'Master Wizard', 'Wizard Lord'],
        'status': ['brass 3', 'silver 3', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 7, 8], [5], [4], [9]],
        'skills': [
            ['channeling (any)', 'dodge', 'intuition', 'language (magick)',
             'lore (magic)', 'melee (basic)', 'melee (polearm)', 'perception'],
            ['charm', 'cool', 'gossip', 'intimidate',
                'language (battle)', 'language (any)'],
            ['animal care', 'evaluate', 'lore (warfare)', 'ride (horse)'],
            ['language (any)', 'lore (any)']
        ],
        'talents':
        [
            ['aethyric attunement', 'petty magic', 'read/write', 'second sight'],
            ['arcane magic (any)', 'detect artefact',
             'fast hands', 'sixth sense'],
            ['dual wielder', 'instinctive diction', 'magical sense', 'menacing'],
            ['combat aware', 'frightening', 'iron will', 'war wizard']
        ],
        'name': 'Wizard',
        'class': 'Academic',
        'trappings': [
            ['grimoire', 'quarterstaff'],
            ['magical license'],
            ['apprentice', 'light warhorse', 'magical item'],
            ['apprentice', 'library (magic)', 'workshop (magic)']
        ]
    },

    ###

    'agitator': {
        'ranks': ['pamphleteer', 'agitator', 'rabble rouser', 'demagogue'],
        'status': ['brass 1', 'brass 2', 'brass 3', 'brass 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[1, 7, 9], [5], [0], [4]],
        'skills': [
            ['art (writing)', 'bribery', 'charm', 'consume alcohol',
             'gossip', 'haggle', 'lore (politics)', 'trade (printing)'],
            ['cool', 'dodge',
                'entertain (storytelling)', 'gamble', 'intuition', 'leadership'],
            ['athletics', 'intimidate', 'melee (brawling)', 'perception'],
            ['lore (heraldry)', 'ride (horse)']
        ],
        'talents':
        [
            ['blather', 'gregarious', 'panhandle', 'read/write'],
            ['alley cat', 'argumentative', 'impassioned zeal', 'public speaker'],
            ['cat-tongued', 'dirty fighting', 'flee!', 'step aside'],
            ['etiquette (any)', 'master orator', 'schemer', 'suave']
        ],
        'name': 'Agitator',
        'class': 'Burgher',
        'trappings': [['writing kit', 'hammer and nails', 'pile of leaflets'],
                      ['leather jack'],
                      ['hand weapon', 'pamphleteer'],
                      ['3 pamphleteers', 'patron', 'printing press', 'impressive hat']]
    },

    'artisan': {
        'ranks': ['Apprentice Artisan', 'Artisan', 'Master Artisan', 'Guildmaster'],
        'status': ['brass 2', 'silver 1', 'silver 3', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2, 3, 6], [9], [8], [7]],
        'skills': [
            ['athletics', 'cool', 'consume alcohol', 'dodge', 'endurance',
                'evaluate', 'stealth (urban)', 'trade (any)'],
            ['charm', 'haggle', 'lore (local)', 'gossip',
             'language (guilder)', 'perception'],
            ['intuition', 'leadership', 'research', 'secret signs (guilder)'],
            ['bribery', 'intimidate']
        ],
        'talents':
        [
            ['artistic', 'craftsman (any)', 'strong back', 'very strong'],
            ['dealmaker', 'etiquette (guilder)', 'nimble fingered', 'sturdy'],
            ['acute sense (taste)|acute sense (touch)',
             'master tradesman (any)', 'read/write', 'tinker'],
            ['briber', 'magnum opus', 'public speaker', 'schemer']
        ],
        'name': 'Artisan',
        'class': 'Burgher',
        'trappings': [['chalk', 'leather jerkin', '2°10|rags'],
                      ['guild licence', 'trade tools'],
                      ['apprentice', 'workshop'],
                      ['guild', 'quality clothing']]
    },

    'beggar': {
        'ranks': ['pauper', 'beggar', 'master beggar', 'beggar king'],
        'status': ['brass 0', 'brass 2', 'brass 4', 'silver 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 5, 9], [8], [0], [4]],
        'skills': [
            ['athletics', 'charm', 'consume alcohol', 'cool',
                'dodge', 'endurance', 'intuition', 'stealth (urban)'],
            ['entertain (acting)', 'entertain (any)', 'gossip',
             'haggle', 'perception', 'sleight of hand'],
            ['charm animal', 'leadership',
                'lore (local)', 'secret signs (vagabond)'],
            ['bribery', 'intimidate']
        ],
        'talents':
        [
            ['panhandle', 'resistance (disease)',
             'stone soup', 'very resilient'],
            ['alley cat', 'beneath notice',
                'criminal', 'etiquette (criminals)'],
            ['blather', 'dirty fighting', 'hardy', 'step aside'],
            ['cat-tongued', 'fearless (watchmen)', 'kingpin', 'suave']
        ],
        'name': 'Beggar',
        'class': 'Burgher',
        'trappings': [
            ['poor quality blanket', 'cup'],
            ['crutch', 'bowl'],
            ['disguise kit', 'hiding place', 'pauper follower'],
            ['lair', 'large group of beggar followers']
        ]
    },

    ###

    'investigator': {
        'ranks': ['sleuth', 'investigator', 'master investigator', 'detective'],
        'status': ['silver 1', 'silver 2', 'silver 3', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[4, 5, 7], [9], [6], [8]],
        'skills': [
            ['charm', 'climb', 'cool', 'gossip', 'intuition',
                'perception', 'stealth (urban)', 'track'],
            ['consume alcohol', 'dodge',
                'lore (law)', 'melee (brawling)', 'pick lock', 'sleight of hand'],
            ['bribery', 'evaluate', 'leadership', 'lore (any)'],
            ['intimidate', 'lore (any)']
        ],
        'talents':
        [
            ['alley cat', 'beneath notice', 'read/write', 'sharp'],
            ['etiquette (any)', 'savvy', 'shadow', 'tenacious'],
            ['bookish', 'break and enter', 'sixth sense', 'suave'],
            ['acute sense (any)', 'savant (any)',
             'speedreader', 'tower of memories']
        ],
        'name': 'Investigator',
        'class': 'Burgher',
        'trappings': [
            ['lantern', 'lamp oil', 'journal', 'quill and ink'],
            ['leather jack', 'hand weapon', 'magnifying glass', 'lockpick'],
            ['assistant', 'office'],
            ['network of informants', 'spyglass']
        ]
    },

    ###

    'merchant': {
        'ranks': ['trader', 'merchant', 'master merchant', 'merchant price'],
        'status': ['silver 2', 'silver 5', 'gold 1', 'gold 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[5, 8, 9], [7], [4], [0]],
        'skills': [
            ['animal care', 'bribery', 'charm', 'consume alcohol',
                'drive', 'gamble', 'gossip', 'haggle'],
            ['evaluate', 'intuition',
                'language (any)', 'language (guilder)', 'lore (local)', 'perception'],
            ['cool', 'language (classical)', 'navigation',
             'secret signs (guilder)'],
            ['lore (any)', 'intimidate']
        ],
        'talents':
        [
            ['blather', 'dealmaker', 'read/write', 'suave'],
            ['briber', 'embezzle', 'etiquette (guilder)', 'savvy'],
            ['cat-tongued', 'etiquette (any)', 'numismatics', 'sharp'],
            ['iron will', 'luck', 'schemer', 'wealthy']
        ],
        'name': 'Merchant',
        'class': 'Burgher',
        'trappings': [
            ['abacus', 'mule and cart', '3°10|shillings'],
            ['riverboat/2 wagons', 'guild license', '20 crowns'],
            ['town house with servants', 'warehouse', '100 crowns'],
            ['2 riverboats%4 wagons', 'large town estate',
                '2 warehouses', '1000 crowns', 'quality clothing']
        ]
    },

    ###

    'rat catcher': {
        'ranks': ['rat hunter', 'rat catcher', 'sewer jack', 'exterminator'],
        'status': ['brass 3', 'silver 1', 'silver 2', 'silver 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 1, 8], [3], [4], [2]],
        'skills': [
            ['athletics', 'animal training (dog)', 'charm animal', 'consume alcohol', 'endurance',
             'melee (basic)', 'ranged (sling)', 'stealth (underground)%stealth (urban)'],
            ['animal care', 'gossip', 'haggle',
                'lore (poison)', 'perception', 'set trap'],
            ['climb', 'cool', 'dodge', 'ranged (crossbow pistol)'],
            ['leadership', 'track']
        ],
        'talents':
        [
            ['night vision', 'resistance (disease)',
             'strike mighty blow', 'strike to stun'],
            ['enclosed fighter',
                'etiquette (guilder)', 'fearless (rats)', 'very resilient'],
            ['hardy', 'stout-hearted', 'strong legs', 'tunnel rat'],
            ['fearless (skaven)', 'menacing', 'robust', 'strong-minded']
        ],
        'name': 'Rat Catcher',
        'class': 'Burgher',
        'trappings': [
            ['sling with ammunition', 'sack', 'small but vicious dog'],
            ['animal traps', 'pole for dead rats'],
            ['davrich lantern', 'hand weapon', 'leather jack'],
            ['assistant', 'large and vicious dog',
                'sack of poisoned bait (10 doses of heartkill)']
        ]
    },

    ###

    'townsman': {
        'ranks': ['clerk', 'townsman', 'town councillor', 'burgomeister'],
        'status': ['silver 1', 'silver 2', 'silver 5', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[9, 7, 5], [4], [6], [8]],
        'skills': [
            ['charm', 'climb', 'consume alcohol', 'drive',
                'dodge', 'gamble', 'gossip', 'haggle'],
            ['bribery', 'evaluate', 'intuition',
                'lore (local)', 'melee (brawling)', 'play (any)'],
            ['cool', 'lore (law)', 'perception', 'research'],
            ['lore (politics)', 'intimidate']
        ],
        'talents':
        [
            ['alley cat', 'beneath notice', 'etiquette (servants)', 'sturdy'],
            ['dealmaker', 'embezzle', 'etiquette (any)', 'gregarious'],
            ['briber', 'public speaker', 'read/write', 'supportive'],
            ['commanding presence', 'master orator', 'schemer', 'suave']
        ],
        'name': 'Townsman',
        'class': 'Burgher',
        'trappings': [
            ['lodging', 'sturdy boots'],
            ['modest townhouse', 'servant', 'quill and ink'],
            ['coach and driver', 'townhouse'],
            ['chains of office', 'coach and footman', 'quality clothing',
                'large townhouse with gardens and servants']
        ]
    },

    ###

    'watchman': {
        'ranks': ['watch recruit', 'watchman', 'watch sergeant', 'watch captain'],
        'status': ['brass 3', 'silver 1', 'silver 3', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 2, 9], [8], [4], [7]],
        'skills': [
            ['athletics', 'climb', 'consume alcohol', 'dodge',
                'endurance', 'gamble', 'melee (any)', 'perception'],
            ['charm', 'cool', 'gossip', 'intimidate',
                'intuition', 'lore (local)'],
            ['entertain (storytelling)', 'haggle', 'leadership', 'lore (law)'],
            ['lore (politics)', 'ride (horse)']
        ],
        'talents':
        [
            ['drilled', 'hardy', 'strike to stun', 'tenacious'],
            ['break and enter', 'criminal', 'night vision', 'sprinter'],
            ['disarm', 'etiquette (soldiers)',
             'fearless (criminals)', 'nose for trouble'],
            ['public speaker', 'robust', 'kingpin', 'schemer']
        ],
        'name': 'Watchman',
        'class': 'Burgher',
        'trappings': [
            ['hand weapon', 'leather jack', 'uniform'],
            ['lantern and pole', 'lamp oil', 'copper badge'],
            ['breastplate', 'helm', 'symbol of rank'],
            ['riding horse with saddle and tack', 'quality hat',
                'quality hand weapon', 'quality symbol of rank']
        ]
    },

    ###

    'advisor': {
        'ranks': ['aide', 'advisor', 'counsellor', 'chancellor'],
        'status': ['silver 2', 'silver 4', 'gold 1', 'gold 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 4, 5], [9], [7], [8]],
        'skills': [
            ['bribery', 'consume alcohol', 'endurance', 'gossip', 'haggle',
                'language (classical)', 'lore (politics)', 'perception'],
            ['charm', 'cool', 'evaluate', 'gamble',
                'intuition', 'lore (local)'],
            ['entertain (storytelling)', 'leadership',
             'language (any)', 'lore (any)'],
            ['lore (heraldry)', 'ride (horse)']
        ],
        'talents':
        [
            ['beneath notice', 'etiquette (any)', 'gregarious', 'read/write'],
            ['blather', 'criminal', 'schemer', 'supportive'],
            ['argumentative', 'briber', 'carouser', 'cat-tongued'],
            ['commanding presence', 'embezzle', 'kingpin', 'suave']
        ],
        'name': 'Advisor',
        'class': 'Courtier',
        'trappings': [
            ['writing kit'],
            ['livery'],
            ['quality clothing', 'aide'],
            ['riding horse with saddle and harness',
                'quality courtly garb', 'staff of advisor and aides']
        ]
    },

    ###

    'artist': {
        'ranks': ['apprentice artist', 'artist', 'master artist', 'maestro'],
        'status': ['silver 1', 'silver 3', 'silver 5', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2, 4, 6], [9], [8], [7]],
        'skills': [
            ['art (any)', 'cool', 'consume alcohol', 'evaluate',
             'endurance', 'gossip', 'perception', 'stealth (urban)'],
            ['climb', 'gamble', 'haggle', 'intuition',
                'language (classical)', 'trade (art supplies)'],
            ['charm', 'leadership', 'lore (art)', 'lore (heraldry)'],
            ['research', 'ride (horse)']
        ],
        'talents':
        [
            ['artistic', 'sharp', 'strong back', 'tenacious'],
            ['carouser', 'criminal', 'gregarious', 'nimble fingered'],
            ['acute sense (any)', 'dealmaker',
             'etiquette (any)', 'nose for trouble'],
            ['ambidextrous', 'kingpin', 'magnum opus', 'read/write']
        ],
        'name': 'Artist',
        'class': 'Courtier',
        'trappings': [
            ['brush%chisel%quill pen'],
            ['sling bag containing trade tools (artist)'],
            ['apprentice', 'patron', 'workshop (artist)'],
            ['large workshop (artist)', 'library (art)', '3 apprentices']
        ]
    },

    ###

    'duellist': {
        'ranks': ['fencer', 'duellist', 'duelmaster', 'judicial champion'],
        'status': ['silver 3', 'silver 5', 'gold 1', 'gold 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 4, 5], [1], [2], [8]],
        'skills': [
            ['athletics', 'dodge', 'endurance', 'heal', 'intuition',
                'language (classical)', 'melee (any)', 'perception'],
            ['charm', 'cool', 'gamble',
                'melee (parry)', 'ranged (blackpowder)', 'trade (gunsmith)'],
            ['intimidate', 'leadership',
                'melee (basic)', 'perform (acrobatics)'],
            ['lore (law)', 'melee (any)']
        ],
        'talents':
        [
            ['beat blade', 'distract', 'feint', 'step aside'],
            ['combat reflexes', 'etiquette (any)', 'fast shot', 'reversal'],
            ['ambidextrous', 'disarm', 'dual wielder', 'riposte'],
            ['combat master', 'menacing', 'reaction strike', 'strike to injure']
        ],
        'name': 'Duellist',
        'class': 'Courtier',
        'trappings': [
            ['1°10| bandages', 'sling bag', 'basic weapon%rapier'],
            ['main gauche%sword-breaker', 'pistol with gunpowder and ammunition'],
            ['quality rapier', 'hand weapon',
                'trusty second', '2 wooden training swords'],
            ['2 quality weapons']
        ]
    },

    ###

    'envoy': {
        'ranks': ['herald', 'envoy', 'diplomat', 'ambassador'],
        'status': ['silver 2', 'silver 4', 'gold 2', 'gold 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 5, 9], [7], [4], [8]],
        'skills': [
            ['athletics', 'charm', 'drive', 'dodge',
                'endurance', 'intuition', 'ride (horse)', 'row'],
            ['art (writing)', 'bribery', 'cool', 'gossip',
             'haggle', 'lore (politics)'],
            ['intimidate', 'language (any)', 'leadership', 'navigation'],
            ['language (any)', 'lore (any)']
        ],
        'talents':
        [
            ['blather', 'etiquette (nobles)', 'read/write', 'suave'],
            ['attractive', 'cat-tongued',
                'etiquette (any)', 'seasoned traveller'],
            ['carouser', 'dealmaker', 'gregarious', 'schemer'],
            ['briber', 'commanding presence', 'noble blood', 'savvy']
        ],
        'name': 'Envoy',
        'class': 'Courtier',
        'trappings': [
            ['leather jack', 'livery', 'scroll case'],
            ['quill and ink', '10 sheets of parchment'],
            ['aide', 'quality clothes', 'map'],
            ['aide', 'best quality couertly clothes',
                'staff of diplomats', 'herald']
        ]
    },

    ###

    'noble': {
        'ranks': ['scion', 'noble', 'magnate', 'noble lord'],
        'status': ['gold 1', 'gold 3', 'gold 5', 'gold 7'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 4, 6], [9], [7], [8]],
        'skills': [
            ['bribery', 'consume alcohol', 'gamble', 'intimidate',
                'leadership', 'lore (heraldry)', 'melee (fencing)', 'play (any)'],
            ['charm', 'gossip',
                'language (classical)', 'lore (local)', 'ride (horse)', 'melee (parry)'],
            ['language (any)', 'intuition', 'lore (politics)', 'perception'],
            ['lore (any)', 'track']
        ],
        'talents':
        [
            ['etiquette (nobles)', 'luck', 'noble blood', 'read/write'],
            ['attractive', 'briber', 'carouser', 'suave'],
            ['coolheaded', 'dealmaker', 'public speaker', 'schemer'],
            ['commanding presence', 'iron will', 'warleader', 'wealthy']
        ],
        'name': 'Noble',
        'class': 'Courtier',
        'trappings': [
            ['courtly garb', 'foil%hand mirror',
                '3°10|crowns worth of jewellery', 'personal servant'],
            ['4 household servants', 'quality courtly garb', 'courtly garb',
                'riding horse with saddle and harness%coach', 'main gauche%quality cloak', '50 crowns worth of jewellery'],
            ['2 sets of quality courtly garb', '200 crowns', 'fiefdom',
                '200 crowns worth of jewellery', 'signet ring'],
            ['4 sets of best quality courtly garb', 'quality foil%hand mirror',
                '500 crowns', '500 crowns worth of jewellery', 'province']
        ]
    },

    ###

    'servant': {
        'ranks': ['menial', 'servant', 'attendant', 'steward'],
        'status': ['silver 1', 'silver 3', 'silver 5', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2, 3, 5], [4], [7], [9]],
        'skills': [
            ['athletics', 'climb', 'drive', 'dodge', 'endurance',
                'intuition', 'perception', 'stealth (any)'],
            ['animal care', 'consume alcohol',
                'evaluate', 'gamble', 'gossip', 'haggle'],
            ['charm', 'cool', 'intimidate', 'lore (local)'],
            ['leadership', 'melee (basic)']
        ],
        'talents':
        [
            ['beneath notice', 'strong back', 'strong-minded', 'sturdy'],
            ['etiquette (servants)', 'shadow', 'tenacious', 'well-prepared'],
            ['embezzle', 'resistance (poison)', 'suave', 'supportive'],
            ['etiquette (any)', 'numismatics', 'read/write', 'savvy']
        ],
        'name': 'Servant',
        'class': 'Courtier',
        'trappings': [
            ['floor brush'],
            ['livery'],
            ['quality livery', 'storm lantern', 'tinderbox', 'lamp oil'],
            ['hand weapon', 'fine clothes', 'servant']
        ]
    },

    ###

    'spy': {
        'ranks': ['informer', 'spy', 'agent', 'spymaster'],
        'status': ['brass 3', 'silver 3', 'gold 1', 'gold 4'],
        #first three are on level 1, then level 2 and so on
        'stats': [[5, 8, 9], [0], [4], [7]],
        'skills': [
            ['bribery', 'charm', 'cool', 'gamble', 'gossip',
                'haggle', 'perception', 'stealth (any)'],
            ['climb', 'entertain (act)', 'intuition', 'melee (basic)',
             'secret signs (any)', 'sleight of hand'],
            ['animal care',
                'animal training (pigeon)', 'language (any)', 'leadership'],
            ['lore (any)', 'research']
        ],
        'talents':
        [
            ['blather', 'carouser', 'gregarious', 'shadow'],
            ['etiquette (any)', 'lip reading',
             'read/write', 'secret identity'],
            ['attractive', 'cat-tongued', 'master of disguise', 'mimic'],
            ['briber', 'schemer', 'suave', 'tower of memories']
        ],
        'name': 'Spy',
        'class': 'Courtier',
        'trappings': [
            ['charcoal stick', 'sling bag',
                '2 different sets of clothing', 'hooded cloak'],
            ['informer', 'hand weapon', 'disguise kit',
                'ring of informers', 'telescope'],
            ['book (cryptography)', 'ring of spies and informers',
             'loft of homing pigeons', 'quill and ink'],
            ['office and staff', 'large spy ring of agents, spies, and informers']
        ]
    },

    ###

    'warden': {
        'ranks': ['custodian', 'warden', 'seneschal', 'governor'],
        'status': ['silver 1', 'silver 3', 'gold 1', 'gold 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2, 3, 8], [0], [9], [7]],
        'skills': [
            ['athletics', 'charm animal', 'consume alcohol', 'cool',
                'endurance', 'intuition', 'lore (local)', 'perception'],
            ['animal care', 'melee (basic)', 'outdoor survival',
             'ranged (bow)', 'ride (horse)', 'swim'],
            ['bribery', 'charm', 'gossip', 'leadership'],
            ['evaluate', 'language (any)']
        ],
        'talents':
        [
            ['menacing', 'night vision', 'sharp', 'strike to stun'],
            ['animal affinity',
                'etiquette (servants)', 'strider (any)', 'rover'],
            ['embezzle', 'numismatics', 'read/write', 'supportive'],
            ['commanding presence',
                'etiquette (any)', 'savant (local)', 'suave']
        ],
        'name': 'Warden',
        'class': 'Courtier',
        'trappings': [
            ['keys', 'lantern', 'lamp oil', 'livery'],
            ['hand weapon%bow with 10 arrows',
                'riding horse with saddle and harness', 'leather jack'],
            ['breastplate', 'ceremonial staff of office',
                'staff of wardens and custodians'],
            ['aide', "governor's residence", 'servant']
        ]
    },

    ###

    'bailiff': {
        'ranks': ['tax collector', 'bailiff', 'reeve', 'magistrate'],
        'status': ['silver 1', 'silver 5', 'gold 1', 'gold 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 4, 8], [9], [5], [7]],
        'skills': [
            ['cool', 'dodge', 'endurance', 'gossip', 'haggle',
                'intimidate', 'melee (basic)', 'perception'],
            ['bribery', 'charm', 'evaluate', 'intuition',
                'leadership', 'lore (local)'],
            ['animal care', 'lore (heraldry)', 'navigation', 'ride (horse)'],
            ['language (classical)', 'lore (law)']
        ],
        'talents':
        [
            ['embezzle', 'numismatics', 'strong back', 'tenacious'],
            ['break and enter', 'criminal', 'public speaking', 'strike to stun'],
            ['kingpin', 'menacing', 'nose for trouble', 'read/write'],
            ['commanding presence', 'iron will', 'savvy', 'schemer']
        ],
        'name': 'Bailiff',
        'class': 'Peasant',
        'trappings': [
            ['hand weapon', 'small lock box'],
            ['leather jack', '3 tax collectors'],
            ['horse with saddle and tack', 'breastplate', 'bailiff'],
            ['library (law)', 'quality robes', 'seal of office']
        ]
    },

    ###

    'hedge witch': {
        'ranks': ['hedge apprentice', 'hedge witch', 'hedge master', 'hedgewise'],
        'status': ['brass 1', 'brass 2', 'brass 3', 'brass 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 4, 6], [7], [9], [8]],
        'skills': [
            ['channeling (hedge)', 'endurance', 'intuition',
                'language (magick)', 'lore (folklore)', 'lore (herbs)', 'outdoor survival', 'perception'],
            ['cool', 'gossip', 'heal',
                'lore (local)', 'trade (charms)', 'trade (herbalist)'],
            ['haggle', 'lore (genealogy)', 'lore (magic)', 'lore (spirits)'],
            ['intimidate', 'pray']
        ],
        'talents':
        [
            ['fast hands', 'petty magic', 'rover', 'strider (woodlands)'],
            ['aethyric attunement', 'animal affinity',
                'arcane magic (hedgecraft)', 'sixth sense'],
            ['craftsman (herbalist)', 'magical sense',
             'pure soul', 'resistance (disease)'],
            ['acute sense (any)', 'master craftsman (herbalist)',
             'night vision', 'strong-minded']
        ],
        'name': 'Hedge Witch',
        'class': 'Peasant',
        'trappings': [
            ['1°10|lucky charms', 'quarterstaff', 'backpack'],
            ['antitoxin kit', 'healing poultice', 'trade tools (herbalist)'],
            ['isolated hut', 'apprentice'],
            ['assortment of animal skulls', 'ceremonial cloak and garland']
        ]
    },

    ###

    'herbalist': {
        'ranks': ['herb gatherer', 'herbalist', 'herb master', 'herbwise'],
        'status': ['brass 2', 'brass 4', 'silvar 1', 'silver 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 4, 5], [6], [9], [7]],
        'skills': [
            ['charm animal', 'climb', 'endurance',
                'lore (herbs)', 'outdoor survival', 'perception', 'swim', 'trade (herbalist)'],
            ['consume alcohol', 'cool', 'gossip',
                'haggle', 'heal', 'lore (local)'],
            ['intuition', 'leadership', 'lore (medicine)', 'trade (poisons)'],
            ['drive', 'navigation']
        ],
        'talents':
        [
            ['acute sense (taste)', 'orientation', 'rover', 'strider (any)'],
            ['dealmaker', 'numble fingered', 'sharp', 'sturdy'],
            ['craftsman (herbalist)', 'field dressing', 'hardy', 'savvy'],
            ['concoct', 'master tradesman (herbalist)',
             'resistance (poison)', 'savant (herbs)']
        ],
        'name': 'Herbalist',
        'class': 'Peasant',
        'trappings': [
            ['boots', 'cloak', 'sling bag', 'assortment of herbs'],
            ['hand weapon (sickle)', 'healing poultice',
             'trade tools (herbalist)'],
            ['herb gatherer', '3 healing poultices',
                'healing draught', 'workshop (herbalist)'],
            ['concoct', 'master tradesman (herbalist)',
             'resistance (poison)', 'savant (herbs)']
        ]
    },

    ###

    'hunter': {
        'ranks': ['trapper', 'hunter', 'tracker', 'huntsmaster'],
        'status': ['brass 2', 'brass 4', 'silver 1', 'silver 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2, 3, 6], [1], [4], [7]],
        'skills': [
            ['charm animal', 'climb', 'endurance',
                'lore (beasts)', 'outdoor survival', 'perception', 'ranged (sling)', 'set trap'],
            ['cool', 'intuition', 'melee (basic)', 'ranged (bow)',
             'secret signs (hunter)', 'stealth (rural)'],
            ['navigation', 'ride (horse)', 'swim', 'track'],
            ['animal care', 'animal training (any)']
        ],
        'talents':
        [
            ['hardy', 'rover', 'strider (any)', 'trapper'],
            ['accurate shot', 'fast shot', "hunter's eye", 'marksman'],
            ['acute sense (any)', 'deadeye shot',
             'fearless (animals)', 'sharpshooter'],
            ['fearless (monsters)', 'robust', 'sniper', 'sure shot']
        ],
        'name': 'Hunter',
        'class': 'Peasant',
        'trappings': [
            ['selection of animal traps', 'hand weapon', 'sturdy boots', 'cloak', 'sling with 10 stone bullets'],
            ['bow', '10 arrows'],
            ['backpack', 'bedroll', 'tent'],
            ['riding horse with saddle and tack', 'kennel of hunting dogs']
        ]
    },

    ###

    'miner': {
        'ranks': ['prospector', 'miner', 'master miner', 'mine foreman'],
        'status': ['brass 2', 'brass 4', 'brass 5', 'silver 4'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2, 3, 8], [0], [4], [9]],
        'skills': [
            ['cool', 'endurance', 'intuition',
                'lore (local)', 'melee (two-handed)', 'outdoor survival', 'perception', 'swim'],
            ['climb', 'consume alcohol', 'evaluate',
                'melee (basic)', 'secret signs (miner)', 'trade (explosives)'],
            ['gossip', 'lore (geology)', 'stealth (underground)',
             'trade (engineer)'],
            ['charm', 'leadership']
        ],
        'talents':
        [
            ['rover', 'strider (rocky)', 'sturdy', 'tenacious'],
            ['night vision', 'strike mighty blow', 'strong back', 'very strong'],
            ['careful strike',
                'craftsman (explosives)', 'tinker', 'tunnel rat'],
            ['argumentative', 'strong-minded', 'embezzle', 'read/write']
        ],
        'name': 'Miner',
        'class': 'Peasant',
        'trappings': [
            ['charcoal stick', 'crude map', 'pan', 'spade'],
            ['davrich lamp', 'hand weapon (pick)', 'lamp oil', 'leather jack'],
            ['great weapon (two-handed pick)', 'helmet',
             'trade tools (engineer)'],
            ['crew of miners', 'writing kit']
        ]
    },

    ###

    'mystic': {
        'ranks': ['fortune teller', 'mystic', 'sage', 'seer'],
        'status': ['brass 1', 'brass 2', 'brass 3', 'brass 4'],
        #first three are on level 1, then level 2 and so on
        'stats': [[4, 6, 9], [8], [5], [7]],
        'skills': [
            ['charm', 'entertain (fortune telling)', 'dodge', 'gossip',
             'haggle', 'intuition', 'perception', 'sleight of hand'],
            ['bribery', 'cool',
                'entertain (prophecy)', 'evaluate', 'intimidate', 'lore (astrology)'],
            ['charm animal', 'entertain (storytelling)',
             'language (any)', 'art (writing)'],
            ['lore (prophecy)', 'channeling (heavens)']
        ],
        'talents':
        [
            ['attractive', 'luck', 'second sight', 'suave'],
            ['detect artefact', 'holy visions', 'sixth sense', 'well-prepared'],
            ['nose for trouble', 'petty magic', 'read/write', 'witch!'],
            ['arcane magic (celestial)', 'magical sense',
             'menacing', 'strong-minded']
        ],
        'name': 'Mystic',
        'class': 'Peasant',
        'trappings': [
            ['deck of cards%set of dice', 'cheap jewellery'],
            ['selection of amulets'],
            ['trade tools (writing)'],
            ['trade tools (astrology)']
        ]
    },

    ###

    'scout': {
        'ranks': ['guide', 'scout', 'pathfinder', 'explorer'],
        'status': ['brass 3', 'brass 5', 'silver 1', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 4, 5], [1], [7], [6]],
        'skills': [
            ['charm animal', 'climb', 'endurance', 'gossip',
                'lore (local)', 'melee (basic)', 'outdoor survival', 'perception'],
            ['athletics', 'navigation',
                'ranged (bow)', 'ride (horse)', 'stealth (rural)', 'track'],
            ['animal care', 'haggle', 'secret signs (hunter)', 'swim'],
            ['language (any)', 'trade (cartographer)']
        ],
        'talents':
        [
            ['orientation', 'rover', 'sharp', 'strider (any)'],
            ['combat aware', 'night vision',
                'nose for trouble', 'seasoned traveller'],
            ['acute sense (sight)', 'sixth sense',
             'strong legs', 'very resilient'],
            ['hardy', 'linguistics', 'savant (local)', 'tenacious']
        ],
        'name': 'Scout',
        'class': 'Peasant',
        'trappings': [
            ['hand weapon', 'leather jack', 'sturdy boots and cloak', 'rope'],
            ['bow', '10 arrows', 'mail shirt'],
            ['map', 'riding horse with saddle and tack',
                "saddlebags with 2 weeks' rations", 'tent'],
            ['selection of maps', 'trade tools (cartographer)']
        ]
    },

    ###

    'villager': {
        'ranks': ['peasant', 'villager', 'councillor', 'village elder'],
        'status': ['brass 2', 'brass 3', 'brass 4', 'silver 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2, 3, 5], [0], [9], [7]],
        'skills': [
            ['animal care', 'athletics', 'consume alcohol', 'endurance',
                'gossip', 'melee (brawling)', 'lore (local)', 'outdoor survival'],
            ['dodge', 'drive', 'entertain (storytelling)',
             'haggle', 'melee (basic)', 'trade (any)'],
            ['bribery', 'charm', 'intimidate', 'leadership'],
            ['intuition', 'lore (history)']
        ],
        'talents':
        [
            ['rover', 'strong back', 'strong-minded', 'stone soup'],
            ['animal affinity', 'hardy', 'tenacious', 'very strong'],
            ['craftsman (any)', 'dealmaker',
             'stout-hearted', 'very resilient'],
            ['master tradesman (any)', 'nimble fingered',
             'public speaker', 'savant (local)']
        ],
        'name': 'Villager',
        'class': 'Peasant',
        'trappings': [
            [''],
            ['leather jerkin', 'hand weapon (axe)', 'trade tools'],
            ['mule and cart', 'village home', 'workshop'],
            ['the respect of the village']
        ]
    },

    ###

    'bounty hunter': {
        'ranks': ['thief-taker', 'bounty hunter', 'master bounty hunter', 'bounty hunter general'],
        'status': ['silver 1', 'silver 3', 'silver 5', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 3, 5], [1], [2], [7]],
        'skills': [
            ['bribery', 'charm', 'gossip', 'haggle', 'intuition',
                'melee (basic)', 'outdoor survival', 'perception'],
            ['athletics', 'endurance', 'intimidate',
                'ranged (crossbow)', 'ranged (entangling)', 'track'],
            ['animal care', 'climb', 'ride (horse)', 'swim'],
            ['drive', 'lore (law)']
        ],
        'talents':
        [
            ['break and enter', 'shadow', 'strike to stun', 'suave'],
            ['marksman', 'relentless', 'seasoned traveller', 'strong back'],
            ['accurate shot', 'careful strike', 'dual wielder', 'sprinter'],
            ['deadeye shot', 'fearless (bounties)', 'hardy', 'sure shot']
        ],
        'name': 'Bounty Hunter',
        'class': 'Ranger',
        'trappings': [
            ['hand weapon', 'leather jerkin', 'rope'],
            ['crossbow', '10 bolts', 'leather skullcap',
                'manacles', 'net', 'warrant papers'],
            ['mail shirt', 'riding horse and saddle'],
            ['draught horse and cart', 'mail shirt', '4 pairs of manacles']
        ]
    },

    ###
    'coachman': {
        'ranks': ['postilion', 'coachman', 'coach master', 'route master'],
        'status': ['silver 1', 'silver 2', 'silver 3', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[1, 3, 8], [5], [0], [4]],
        'skills': [
            ['animal care', 'charm animal', 'climb', 'drive', 'endurance',
                'perception', 'ranged (entangling)', 'ride (horse)'],
            ['consume alcohol', 'gossip', 'intuition',
                'lore (local)', 'navigation', 'ranged (blackpowder)'],
            ['animal training (horse)', 'intimidate',
             'language (any)', 'lore (routes)'],
            ['charm', 'leadership']
        ],
        'talents':
        [
            ['animal affinity', 'seasoned traveller', 'trick-riding', 'tenacious'],
            ['coolheaded', 'crack the whip', 'gunner', 'strong-minded'],
            ['accurate shot', 'dealmaker',
                'fearless (outlaws)', 'nose for trouble'],
            ['fearless (beastmen)', 'marksman', 'orientation', 'rapid reload']
        ],
        'name': 'Coachman',
        'class': 'Ranger',
        'trappings': [
            ['warm coat and gloves', 'whip'],
            ['blunderbuss with 10 shots', 'coach horn', 'leather jack', 'hat'],
            ['mail shirt', 'pistol', 'quality cloak'],
            ['fleet of coaches and horses', 'maps']
        ]
    },


    ###
    'entertainer': {
        'ranks': ['busker', 'entertainer', 'troubadour', 'troupe leader'],
        'status': ['brass 3', 'brass 5', 'silver 3', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[5, 6, 9], [0], [1], [3]],
        'skills': [
            ['athletics', 'charm', 'entertain (any)', 'gossip', 'haggle',
             'perform (any)', 'play (any)', 'sleight of hand'],
            ['entertain (any)', 'ride (any)', 'melee (basic)',
             'perform (any)', 'play (any)', 'ranged (throwing)'],
            ['animal care', 'animal training (any)',
                'art (writing)', 'language (any)'],
            ['drive', 'leadership']
        ],
        'talents':
        [
            ['attractive', 'mimic', 'public-speaking', 'suave'],
            ['contortionist', 'jump up', 'sharpshooter', 'trick riding'],
            ['blather', 'master of disguise', 'perfect pitch', 'read/write'],
            ['dealmaker', 'etiquette (any)', 'seasoned traveller', 'sharp']
        ],
        'name': 'Entertainer',
        'class': 'Ranger',
        'trappings': [
            ['bowl', 'instrument'],
            ['costume', 'instrument',
                "selection of scripts (that you can't yet read)", 'throwing weapons'],
            ['trained animal', 'writing kit'],
            ['draught horses and wagon (stage)',
             'wardrobe of costumes and props', 'troupe of entertainers']
        ]
    },

    ###
    'flagellant': {
        'ranks': ['zealot', 'flagellant', 'penitent', 'prophet of doom'],
        'status': ['brass 0', 'brass 0', 'brass 0', 'brass 0'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 2, 3], [8], [4], [9]],
        'skills': [
            ['dodge', 'endurance', 'heal', 'intimidate', 'intuition',
                'lore (sigmar)', 'melee (flail)', 'outdoor survival'],
            ['art (icons)', 'athletics', 'cool', 'language (classical)',
             'lore (the empire)', 'ranged (sling)'],
            ['charm', 'language (any)', 'lore (theology)', 'perception'],
            ['entertain (speeches)', 'leadership']
        ],
        'talents':
        [
            ['berserk charge', 'frenzy', 'read/write', 'stone soup'],
            ['hardy', 'hatred (heretics)', 'flagellant', 'implacable'],
            ['field dressing', 'furious assault',
                'menacing', 'seasoned traveller'],
            ['battle rage', 'fearless (heretics)',
             'frightening', 'impassioned zeal']
        ],
        'name': 'Flagellant',
        'class': 'Ranger',
        'trappings': [
            ['flail', 'tattered robes'],
            ['placard', 'religious symbol', 'sling'],
            ['religious relic'],
            ['book (religion)',
             'followers (including penitents, flagellants, and zealots)']
        ]
    },

    ###
    'messenger': {
        'ranks': ['runner', 'messenger', 'courier', 'courier-captain'],
        'status': ['brass 3', 'silver 1', 'silver 3', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 4, 5], [0], [8], [9]],
        'skills': [
            ['athletics', 'climb', 'dodge', 'endurance', 'gossip',
                'navigation', 'perception', 'melee (brawling)'],
            ['animal care', 'charm', 'cool',
                'lore (local)', 'melee (basic)', 'ride (horse)'],
            ['charm animal', 'bribery', 'consume alcohol', 'outdoor survival'],
            ['intimidate', 'leadership']
        ],
        'talents':
        [
            ['flee!', 'fleet footed', 'sprinter', 'step aside'],
            ['crack the whip', 'criminal', 'orientation', 'seasoned traveller'],
            ['nose for trouble', 'relentless', 'tenacious', 'trick rider'],
            ['dealmaker', 'hatred (outlaws)', 'kingpin', 'very resilient']
        ],
        'name': 'Messenger',
        'class': 'Ranger',
        'trappings': [
            ['scroll case'],
            ['hand weapon', 'leather jack', 'riding horse with saddle and tack'],
            ['backpack', 'saddlebags', 'shield'],
            ['couriers', 'mail shirt', 'writing kit']
        ]
    },

    ###
    'pedlar': {
        'ranks': ['vagabond', 'pedlar', 'master pedlar', 'wandering trader'],
        'status': ['brass 1', 'brass 4', 'silver 1', 'silver 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 6, 8], [9], [4], [7]],
        'skills': [
            ['charm', 'endurance', 'entertain (storytelling)', 'gossip', 'haggle',
             'intuition', 'outdoor survival', 'stealth (urban)%stealth (rural)'],
            ['animal care', 'charm animal', 'consume alcohol',
                'evaluate', 'ride (horse)', 'trade (tinker)'],
            ['drive', 'intimidate', 'language (any)', 'perception'],
            ['lore (local)', 'lore (geography)']
        ],
        'talents':
        [
            ['fisherman', 'flee!', 'rover', 'tinker'],
            ['dealmaker', 'orientation', 'seasoned traveller', 'strong back'],
            ['numismatics', 'sturdy', 'well-prepared', 'very resilient'],
            ['cat-tongued', 'strong-minded', 'suave', 'tenacious']
        ],
        'name': 'Pedlar',
        'class': 'Ranger',
        'trappings': [
            ['backpack', 'bedroll', '2°10|brass worth of goods', 'tent'],
            ['mule and saddlebags', '2°10|silver worth of goods',
                'selection of pots and pans', 'trade tools (tinker)'],
            ['cart', '2°10|gold worth of goods'],
            ['draught horse and wagon', '5°10|gold worth of goods', '50 shillings']
        ]
    },

    ###
    'road warden': {
        'ranks': ['toll keeper', 'road warden', 'road sergeant', 'road captain'],
        'status': ['brass 5', 'silver 2', 'silver 4', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[1, 3, 4], [0], [9], [7]],
        'skills': [
            ['bribery', 'consume alcohol', 'gamble', 'gossip', 'haggle',
                'melee (basic)', 'perception', 'ranged (crossbow)'],
            ['animal care', 'endurance', 'intimidate',
                'intuition', 'outdoor survival', 'ride (horse)'],
            ['athletics', 'charm', 'leadership', 'ranged (blackpowder)'],
            ['lore (empire)', 'navigation']
        ],
        'talents':
        [
            ['coolheaded', 'embezzle', 'marksman', 'numismatics'],
            ['crack the whip', 'criminal', 'roughrider', 'seasoned traveller'],
            ['etiquette (soldiers)', 'fearless (outlaws)',
             'hatred (any)', 'nose for trouble'],
            ['combat aware', 'commanding presence', 'kingpin', 'public speaker']
        ],
        'name': 'Road Warden',
        'class': 'Ranger',
        'trappings': [
            ['crossbow', '10 bolts', 'leather jack'],
            ['hand weapon', 'mail shirt',
                'riding horse with saddle and harness', 'rope'],
            ['squad of road wardens', 'pistol',
                '10 shots', 'shield', 'symbol of rank'],
            ['light warhorse', 'pistol', '10 shots',
                'quality hat and cloak', 'unit of road wardens']
        ]
    },

    ###

    'witch hunter': {
        'ranks': ['interrogator', 'witch hunter', 'inquisitor', 'witchfinder general'],
        'status': ['silver 1', 'silver 3', 'silver 5', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 3, 8], [1], [9], [7]],
        'skills': [
            ['charm', 'consume alcohol', 'heal', 'intimidate', 'intuition',
                'lore (torture)', 'melee (brawling)', 'perception'],
            ['cool', 'melee (basic)', 'gossip',
                'lore (witches)', 'ranged (any)', 'ride (horse)'],
            ['endurance', 'leadership', 'lore (law)', 'lore (local)'],
            ['lore (chaos)', 'lore (politics)']
        ],
        'talents':
        [
            ['coolheaded', 'menacing', 'read/write', 'resolute'],
            ['dual wielder', 'marksman', 'seasoned traveller', 'shadow'],
            ['fearless (witches)', 'nose for trouble',
             'relentless', 'strong-minded'],
            ['frightening', 'iron will', 'magical sense', 'pure soul']
        ],
        'name': 'Witch Hunter',
        'class': 'Ranger',
        'trappings': [
            ['hand weapon', 'instruments of torture'],
            ['crossbow pistol%pistol', 'hat (henin)', 'leather jack',
             'riding horse with saddle and tack', 'rope', 'silvered sword'],
            ['quality clothing', 'subordinate interrogators'],
            ['best quality courtly garb', 'subordinate witch hunters']
        ]
    },

    ###

    'boatman': {
        'ranks': ['boat-hand', 'boatman', 'bargeswain', 'barge master'],
        'status': ['silver 1', 'silver 2', 'silver 3', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2, 3, 5], [4], [6], [7]],
        'skills': [
            ['consume alcohol', 'dodge', 'endurance', 'gossip',
                'melee (brawling)', 'row', 'sail', 'swim'],
            ['athletics', 'entertain (storytelling)', 'haggle',
             'intuition', 'lore (riverways)', 'perception'],
            ['climb', 'entertain (singing)', 'heal', 'trade (boatbuilding)'],
            ['leadership', 'navigation']
        ],
        'talents':
        [
            ['dirty fighting', 'fisherman', 'strong back', 'strong swimmer'],
            ['etiquette (guilder)', 'seasoned traveller',
             'very strong', 'waterman'],
            ['dealmaker', 'embezzle', 'nose for trouble', 'strike mighty blow'],
            ['menacing', 'orientation', 'pilot', 'public speaker']
        ],
        'name': 'Boatman',
        'class': 'Riverfolk',
        'trappings': [
            ['hand weapon (boat hook)', 'leather jack', 'pole'],
            ['rope', 'rowboat'],
            ['backpack', 'trade tools (carpenter)'],
            ['hat', 'riverboat and crew']
        ]
    },

    ###

    'huffer': {
        'ranks': ['riverguide', 'huffer', 'pilot', 'master pilot'],
        'status': ['brass 4', 'silver 1', 'silver 3', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 3, 4], [8], [7], [9]],
        'skills': [
            ['consume alcohol', 'gossip', 'intuition',
                'lore (local)', 'lore (riverways)', 'perception', 'row', 'swim'],
            ['charm', 'cool', 'entertain (storytelling)',
             'language (any)', 'melee (basic)', 'navigation'],
            ['haggle', 'intimidate', 'lore (local)', 'lore (wrecks)'],
            ['leadership', 'sail']
        ],
        'talents':
        [
            ['fisherman', 'night vision', 'orientation', 'waterman'],
            ['dealmaker', 'etiquetter (guilder)',
             'noser for trouble', 'river guide'],
            ['acute sense (sight)', 'pilot', 'sea legs', 'very strong'],
            ['sixth sense', 'sharp', 'strong swimmer', 'tenacious']
        ],
        'name': 'Huffer',
        'class': 'Riverfolk',
        'trappings': [
            ['hand weapon (boat hook)', 'storm lantern and oil'],
            ['leather jerkin', 'rope', 'row boat'],
            ['pole', 'storm lantern and oil'],
            ['boathand', 'small riverboat']
        ]
    },

    ###

    'riverwarden': {
        'ranks': ['river recruit', 'riverwarden', 'shipsword', 'shipsword master'],
        'status': ['silver 1', 'silver 2', 'silver 4', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[1, 2, 9], [0], [4], [7]],
        'skills': [
            ['athletics', 'dodge', 'endurance',
                'melee (basic)', 'perception', 'row', 'sail', 'swim'],
            ['bribery', 'charm', 'intimidate', 'gossip',
                'lore (riverways)', 'ranged (blackpowder)'],
            ['climb', 'cool', 'intuition', 'leadership'],
            ['lore (law)', 'navigation']
        ],
        'talents':
        [
            ['strong swimmer', 'strong back', 'very strong', 'waterman'],
            ['criminal', 'gunner', 'fisherman', 'seasoned traveller'],
            ['fearless (wreckers)', 'hatred (any)', 'pilot', 'sea legs'],
            ['commanding presence', 'kingpin', 'menacing', 'orientation']
        ],
        'name': 'Riverwarden',
        'class': 'Riverfolk',
        'trappings': [
            ['hand weapon (sword)', 'leather jack', 'uniform'],
            ['lantern and oil', 'pistol with 10 shots', 'shield'],
            ['grappling hook', 'helmet', 'mail shirt'],
            ['patrol boats and crew', 'symbol of rank']
        ]
    },

    ###

    'riverwoman': {
        'ranks': ['greenfish', 'riverwoman', 'riverwise', 'river elder'],
        'status': ['brass 2', 'brass 3', 'brass 5', 'silver 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3, 5, 6], [0], [4], [9]],
        'skills': [
            ['athletics', 'consume alcohol', 'dodge', 'endurance',
                'gossip', 'outdoor survival', 'row', 'swim'],
            ['gamble', 'lore (local)', 'lore (riverways)',
             'ranged (entangling)', 'ranged (throwing)', 'set trap'],
            ['charm', 'intuition', 'melee (polearm)', 'perception'],
            ['entertain (storytelling)', 'lore (folklore)']
        ],
        'talents':
        [
            ['fisherman', 'gregarious', 'strider (marshes)', 'strong swimmer'],
            ['craftsman (boatbuilder)', 'rover', 'strong back', 'waterman'],
            ['savant (riverways)', 'stout-hearted',
             'tenacious', 'very strong'],
            ['master craftsman (boatbuilder)', 'public speaker',
             'sharp', 'strong-minded']
        ],
        'name': 'Riverwoman',
        'class': 'Riverfolk',
        'trappings': [
            ['bucket', 'fishing rod and bait', 'leather leggings'],
            ['eel trap', 'leather jerkin', 'net', 'spear'],
            ['row boat', 'storm lantern and oil'],
            ['hut%riverboat']
        ]
    },

    ###

    'seaman': {
        'ranks': ['landsman', 'seaman', 'boatswain', "ship's master"],
        'status': ['silver 1', 'silver 3', 'silver 5', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[5, 6, 9], [0], [4], [7]],
        'skills': [
            ['climb', 'consume alcohol', 'gamble', 'gossip',
                'row', 'melee (brawling)', 'sail', 'swim'],
            ['athletics', 'dodge', 'endurance',
                'entertain (singing)', 'language (any)', 'melee (basic)'],
            ['cool', 'leadership', 'perception', 'trade (carpenter)'],
            ['charm', 'navigation']
        ],
        'talents':
        [
            ['fisherman', 'strider (coastal)',
             'strong back', 'strong swimmer'],
            ['catfall', 'sea legs', 'seasoned traveller', 'strong legs'],
            ['old salt', 'strike mighty blow', 'tenacious', 'very strong'],
            ['orientation', 'pilot', 'public speaking', 'savvy']
        ],
        'name': 'Seaman',
        'class': 'Riverfolk',
        'trappings': [
            ['bucket', 'brush', 'mop'],
            ['hand weapon (boat hook)', 'leather jerkin'],
            ['trade tools (carpenter)'],
            ['shipping charts', 'sailing ship and crew', 'sextant', 'spyglass']
        ]
    },

    ###

    'smuggler': {
        'ranks': ['river runner', 'smuggler', 'master smuggler', 'smuggler king'],
        'status': ['brass 2', 'brass 3', 'brass 5', 'silver 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[5, 6, 8], [4], [7], [9]],
        'skills': [
            ['athletics', 'bribery', 'cool', 'consume alcohol', 'row',
                'sail', 'stealth (rural)%stealth (urban)', 'swim'],
            ['haggle', 'gossip', 'lore (local)', 'melee (basic)',
             'perception', 'secret signs (smuggler)'],
            ['evaluate', 'intimidate', 'intuition', 'lore (riverways)'],
            ['language (any)', 'leadership']
        ],
        'talents':
        [
            ['criminal', 'fisherman', 'strider (marshes)', 'strong back'],
            ['dealmaker', 'etiquette (criminals)', 'waterman', 'very strong'],
            ['briber', 'fearless (riverwardens)', 'pilot', 'strong swimmer'],
            ['kingpin', 'savvy', 'strider (coastal)', 'sea legs']
        ],
        'name': 'Smuggler',
        'class': 'Riverfolk',
        'trappings': [
            ['large sack', 'mask%scarves', 'tinderbox', 'storm lantern and oil'],
            ['2 barrels,', 'hand weapon', 'leather jack', 'row boat'],
            ['river runner', 'speedy riverboat'],
            ['disguise kit', 'small fleet of riverboats']
        ]
    },

    ###

    'stevedore': {
        'ranks': ['dockhand', 'stevedore', 'foreman', 'dock master'],
        'status': ['brass 3', 'silver 1', 'silver 3', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 3, 4], [2], [8], [7]],
        'skills': [
            ['athletics', 'climb', 'consume alcohol', 'dodge',
                'endurance', 'gossip', 'melee (basic)', 'swim'],
            ['bribery', 'entertain (storytelling)', 'gamble',
             'intimidate', 'perception', 'stealth (urban)'],
            ['cool', 'evaluate', 'intuition', 'leadership'],
            ['charm', 'lore (taxes)']
        ],
        'talents':
        [
            ['dirty fighting', 'strong back', 'sturdy', 'very strong'],
            ['criminal', 'etiquette (guilders)', 'strong legs', 'tenacious'],
            ['dealmaker', 'embezzle',
                'etiquette (criminals)', 'public speaking'],
            ['kingpin', 'menacing', 'numismatics', 'read/write']
        ],
        'name': 'Stevedore',
        'class': 'Riverfolk',
        'trappings': [
            ['hand weapon (boat hook)', 'leather gloves'],
            ['guild licence', 'leather jerkin', 'pipe and tobacco', 'porter cap'],
            ['gang of stevedores', 'whistle'],
            ['office and staff', 'writing kit']
        ]
    },

    ###

    'wrecker': {
        'ranks': ['cargo scavenger', 'wrecker', 'river pirate', 'wrecker captain'],
        'status': ['brass 2', 'brass 3', 'brass 5', 'silver 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 2, 4], [8], [1], [9]],
        'skills': [
            ['climb', 'consume alcohol', 'dodge', 'endurance',
                'row', 'melee (basic)', 'outdoor survival', 'swim'],
            ['bribery', 'cool', 'intuition', 'navigation', 'perception', 'set trap'],
            ['gossip', 'intimidate', 'ranged (crossbow)', 'stealth (rural)'],
            ['leadership', 'lore (riverways)']
        ],
        'talents':
        [
            ['break and enter', 'criminal', 'fisherman', 'strong back'],
            ['flee!', 'rover', 'strong swimmer', 'trapper'],
            ['dirty fighting',
                'etiquette (criminals)', 'menacing', 'waterman'],
            ['furious assault', 'in-fighter', 'pilot', 'warrior born']
        ],
        'name': 'Wrecker',
        'class': 'Riverfolk',
        'trappings': [
            ['crowbar', 'large sack', 'leather gloves'],
            ['hand weapon (boat hook)', 'leather jack',
             'storm lantern and oil'],
            ['crossbow with 10 bolts', 'grappling hook and rope', 'riverboat'],
            ['fleet of riverboats', 'wrecker crew', 'keg of ale', 'manacles']
        ]
    },

    ###

    'bawd': {
        'ranks': ['hustler', 'bawd', 'procurer', 'ringleader'],
        'status': ['brass 1', 'brass 3', 'silver 1', 'silver 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[5, 6, 9], [4], [8], [7]],
        'skills': [
            ['bribery', 'charm', 'consume alcohol',
                'entertain (any)', 'gamble', 'gossip', 'haggle', 'intimidate'],
            ['dodge', 'endurance', 'intuition',
                'lore (local)', 'melee (basic)', 'perception'],
            ['cool', 'evaluate', 'language (any)', 'lore (law)'],
            ['leadership', 'lore (heraldry)']
        ],
        'talents':
        [
            ['attractive', 'alley cat', 'blather', 'gregarious'],
            ['ambidextrous', 'carouser', 'criminal', 'resistant (disease)'],
            ['dealmaker', 'embezzle', 'etiquette (any)', 'suave'],
            ['briber', 'kingpin', 'numismatics', 'savvy']
        ],
        'name': 'Bawd',
        'class': 'Rogue',
        'trappings': [
            ['flask of spirits'],
            ['dose of weirdroot', 'quality clothing'],
            ['a ring of hustlers'],
            ['townhouse with discreet back entrance', 'a ring of bawds']
        ]
    },
    ###

    'charlatan': {
        'ranks': ['swindler', 'charlatan', 'con artist', 'scoundrel'],
        'status': ['brass 3', 'brass 5', 'silver 2', 'silver 4'],
        #first three are on level 1, then level 2 and so on
        'stats': [[4, 6, 9], [8], [5], [7]],
        'skills': [
            ['bribery', 'consume alcohol', 'charm',
                'entertain (storytelling)', 'gamble', 'gossip', 'haggle', 'sleight of hand'],
            ['cool', 'dodge', 'entertain (acting)',
             'evaluate', 'intuition', 'perception'],
            ['language (thief)', 'lore (heraldry)',
             'pick lock', 'secret signs (thief)'],
            ['lore (genealogy)', 'research']
        ],
        'talents':
        [
            ['cardsharp', 'diceman', 'etiquette (any)', 'luck'],
            ['blather', 'criminal', 'fast hands', 'secret identity'],
            ['attractive', 'cat-tongued', 'dealmaker', 'read/write'],
            ['gregarious', 'master of disguise', 'nose for trouble', 'suave']
        ],
        'name': 'Charlatan',
        'class': 'Rogue',
        'trappings': [
            ['backpack', '2 sets of clothing', 'deck of cards', 'dice'],
            ['forged document', '2 sets of quality clothing',
                'selection of coloured powders and water', 'selection of trinkets and charms'],
            ['disguise kit', 'lock picks', 'multiple forged documents'],
            ['forged seal', 'writing kit']
        ]
    },

    ###

    'fence': {
        'ranks': ['broker', 'fence', 'master fence', 'black marketeer'],
        'status': ['silver 1', 'silver 2', 'silver 3', 'silver 4'],
        #first three are on level 1, then level 2 and so on
        'stats': [[4, 5, 9], [6], [7], [8]],
        'skills': [
            ['charm', 'consume alcohol', 'dodge', 'evaluate',
                'gamble', 'gossip', 'haggle', 'melee (basic)'],
            ['cool', 'intimidate', 'intuition', 'perception',
                'secret signs (thief)', 'trade (engraver)'],
            ['bribery', 'entertain (storytelling)',
             'lore (art)', 'lore (local)'],
            ['lore (heraldry)', 'research']
        ],
        'talents':
        [
            ['alley cat', 'cardsharp', 'dealmaker', 'gregarious'],
            ['criminal', 'etiquette (criminals)', 'numismatics', 'savvy'],
            ['kingpin', 'strike to stun', 'suave', 'super numerate'],
            ['dirty fighting', 'iron will', 'menacing', 'briber']
        ],
        'name': 'Fence',
        'class': 'Rogue',
        'trappings': [
            ['hand weapon', '3°10|shillings worth of stolen goods'],
            ['eye-glass', 'trade tools (engraver)', 'writing kit'],
            ["pawnbroker's shop"],
            ['hired muscle', 'network of informants', 'warehouse']
        ]
    },

    ###

    'grave robber': {
        'ranks': ['body snatcher', 'grave robber', 'tomb robber', 'treasure hunter'],
        'status': ['brass 2', 'brass 3', 'silver 1', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2, 4, 8], [0], [6], [7]],
        'skills': [
            ['climb', 'cool', 'dodge', 'drive', 'gossip',
                'intuition', 'perception', 'stealth (any)'],
            ['bribery', 'endurance', 'evaluate', 'haggle',
                'lore (medicine)', 'melee (basic)'],
            ['lore (history)', 'pick lock','research', 'set trap'],
            ['navigation', 'trade (engineer)']
        ],
        'talents':
        [
            ['alley cat', 'criminal', 'flee!', 'strong back'],
            ['break and enter', 'night vision',
                'resistance (disease)', 'very strong'],
            ['read/write', 'strike mighty blow', 'tenacious', 'tuneel rat'],
            ['fearless (undead)', 'sixth sense', 'strong-minded', 'trapper']
        ],
        'name': 'Grave Robber',
        'class': 'Rogue',
        'trappings': [
            ['crowbar', 'handcart', 'hooded cloak', 'tarpaulin'],
            ['backpack', 'hand weapon', 'spade', 'storm lantern and oil'],
            ['hand weapon (pick)', 'horse and cart',
             'leather jack', 'rope', 'trade tools (thief)'],
            ['bedroll', 'maps', 'tent',
                'trade tools (engineer)', 'writing kit']
        ]
    },

    ###

    'outlaw': {
        'ranks': ['brigand', 'outlaw', 'outlaw chief', 'bandit king'],
        'status': ['brass 1', 'brass 2', 'brass 4', 'silver 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 2, 3], [1], [4], [9]],
        'skills': [
            ['athletics', 'consume alcohol', 'cool', 'endurance', 'gamble',
                'intimidate', 'melee (basic)', 'outdoor survival'],
            ['dodge', 'heal', 'lore (local)', 'perception',
             'ranged (bow)', 'stealth (rural)'],
            ['gossip', 'intuition', 'leadership', 'ride (horse)'],
            ['charm', 'lore (empire)']
        ],
        'talents':
        [
            ['combat aware', 'criminal', 'rover', 'flee!'],
            ['dirty fighting', 'marksman', 'strike to stun', 'trapper'],
            ['rapid reload', 'roughrider', 'menacing', 'very resilient'],
            ['deadeye shot', 'fearless (road wardens)', 'iron will', 'robust']
        ],
        'name': 'Outlaw',
        'class': 'Rogue',
        'trappings': [
            ['bedroll', 'hand weapon', 'leather jerkin', 'tinderbox'],
            ['bow with 10 arrows', 'shield', 'tent'],
            ['helmet', 'riding horse with saddle and tack',
                'sleeved mail shirt', 'band of outlaws'],
            ["'fiefdom' of outlaw chiefs", 'lair']
        ]
    },

    ###

    'racketeer': {
        'ranks': ['thug', 'racketeer', 'gang boss', 'crime lord'],
        'status': ['brass 3', 'brass 5', 'silver 3', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 2, 3], [9], [8], [7]],
        'skills': [
            ['consume alcohol', 'cool', 'dodge', 'endurance', 'intimidate',
                'lore (local)', 'melee (brawling)', 'stealth (urban)'],
            ['bribery', 'charm', 'evaluate', 'gossip',
                'language (estalian)%language (tilean)', 'melee (basic)'],
            ['intuition', 'leadership', 'perception', 'ranged (crossbow)'],
            ['lore (law)', 'lore (politics']
        ],
        'talents':
        [
            ['criminal', 'etiquette (criminals)',
             'menacing', 'strike mighty blow'],
            ['embezzle', 'dirty fighting', 'strike to stun', 'warrior born'],
            ['fearless (watchmen)', 'iron will',
             'resistance (poison)', 'robust'],
            ['commanding presence', 'kingpin', 'frightening', 'wealthy']
        ],
        'name': 'Racketeer',
        'class': 'Rogue',
        'trappings': [
            ['knuckledusters', 'leather jack'],
            ['hand weapon', 'hat', 'mail shirt'],
            ['crossbow pistol with 10 bolts',
                'gang of thugs and racketeers', 'lair'],
            ['network of informers', 'quality clothing and hat',
                'subordinate gang bosses']
        ]
    },

    ###

    'thief': {
        'ranks': ['prowler', 'thief', 'master thief', 'cat burglar'],
        'status': ['brass 1', 'brass 3', 'brass 5', 'silver 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[4, 5, 8], [6], [2], [9]],
        'skills': [
            ['athletics', 'climb', 'cool', 'dodge', 'endurance',
                'intuition', 'perception', 'stealth (urban)'],
            ['evaluate', 'gossip',
                'lore (local)', 'pick lock', 'secret signs (thief)', 'sleight of hand'],
            ['bribery', 'gamble', 'intimidate', 'ranged (crossbow)'],
            ['charm', 'set trap']
        ],
        'talents':
        [
            ['alley cat', 'criminal', 'flee!', 'strike to stun'],
            ['break and enter',
                'etiquette (criminal)', 'fast hands', 'shadow'],
            ['night vision', 'nimble fingered', 'step aside', 'trapper'],
            ['catfall', 'scale sheer surface', 'strong legs', 'wealthy']
        ],
        'name': 'Thief',
        'class': 'Rogue',
        'trappings': [
            ['crowbar', 'leather jerkin', 'sack'],
            ['trade tools (thief)', 'rope'],
            ['crossbow pistol with 10 bolts', 'throwing knives'],
            ['dark clothing', 'grappling hook', 'mask%scarves']
        ]
    },

    ###

    'witch': {
        'ranks': ['hexer', 'witch', 'wyrd', 'warlock'],
        'status': ['brass 1', 'brass 2', 'brass 3', 'brass 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 3, 8], [4], [9], [7]],
        'skills': [
            ['channeling (witchcraft)', 'cool', 'endurance', 'gossip', 'intimidate',
                'language (magick)', 'sleight of hand', 'stealth (rural)'],
            ['charm animal', 'dodge', 'intuition',
                'melee (polearm)', 'perception', 'trade (herbalist)'],
            ['bribery','charm','haggle','lore (dark magic)'],
            ['lore (daemonology)', 'lore (magic)']
        ],
        'talents':
        [
            ['criminal', 'instinctive diction', 'menacing', 'petty magic'],
            ['arcane magic (witchery)', 'attractive', 'sixth sense', 'witch!'],
            ['animal affinity', 'fast hands', 'frightening', 'magical sense'],
            ['aethyric attunement', 'luck', 'strong-minded', 'very resilient']
        ],
        'name': 'Witch',
        'class': 'Rogue',
        'trappings': [
            ['candles', 'chalk', 'doll', 'pins'],
            ['quarterstaff', 'sack', 'selection of herbs',
                'trade tools (herbalist)'],
            ['backpack', 'cloak with several pockets', 'lucky charm'],
            ['robes', 'skull']
        ]
    },


    ###

    'cavalryman': {
        'ranks': ['horseman', 'cavalryman', 'cavalry sergeant', 'cavalry officer'],
        'status': ['silver 2', 'silver 4', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 2, 5], [1], [4], [9]],
        'skills': [
            ['animal care', 'charm animal', 'endurance',
                'language (battle)', 'melee (basic)', 'outdoor survival', 'perception', 'ride (horse)'],
            ['charm', 'consume alcohol', 'cool', 'gossip',
                'melee (cavalry)', 'ranged (blackpowder)'],
            ['intimidate', 'intuition', 'leadership', 'lore (warfare)'],
            ['gamble', 'lore (heraldry)']
        ],
        'talents':
        [
            ['combat aware', 'crack the whip', 'lightning reflexes', 'roughrider'],
            ['etiquette (soldiers)', 'gunner',
             'seasoned traveller', 'trick riding'],
            ['combat reflexes', 'fast shot', 'hatred (any)', 'warleader'],
            ['accurate shot', 'inspiring', 'reaction strike', 'robust']
        ],
        'name': 'Cavalryman',
        'class': 'Warrior',
        'trappings': [
            ['leather jack', 'riding horse with saddle and tack'],
            ['breastplate', 'demilance', 'helmet',
                'light warhorse with saddle and tack', 'pistol with 10 shots', 'shield'],
            ['sash'],
            ['deck of cards', 'quality clothing']
        ]
    },

    ###

    'guard': {
        'ranks': ['sentry', 'guard', 'honour guard', 'guard officer'],
        'status': ['silver 1', 'silver 2', 'silver 3', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 3, 5], [4], [2], [7]],
        'skills': [
            ['consume alcohol', 'endurance',
                'entertain (storytelling)', 'gamble', 'gossip', 'intuition', 'melee (basic)', 'perception'],
            ['athletics', 'cool', 'dodge', 'intimidate',
                'melee (polearm)', 'ranged (bow)'],
            ['heal', 'language (battle)', 'lore (etiquette)',
             'melee (two-handed)'],
            ['leadership', 'lore (warfare)']
        ],
        'talents':
        [
            ['diceman', 'etiquette (servants)', 'strike to stun', 'tenacious'],
            ['relentless', 'reversal', 'shieldsman', 'strike mighty blow'],
            ['fearless (intruders)', 'jump up',
             'stout-hearted', 'unshakeable'],
            ['combat master', 'furious assault', 'iron will', 'robust']
        ],
        'name': 'Guard',
        'class': 'Warrior',
        'trappings': [
            ['buckler', 'leather jerkin', 'storm lantern with oil'],
            ['bow with 10 arrows', 'sleeved mail shirt', 'shield', 'spear'],
            ['great weapon%halberd', 'helmet', 'uniform'],
            ['breastplate']
        ]
    },

    ###

    'knight': {
        'ranks': ['squire', 'knight', 'first knight', 'knight of the inner circle'],
        'status': ['silver 3', 'silver 5', 'gold 2', 'gold 4'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2, 4, 5], [0], [8], [9]],
        'skills': [
            ['athletics', 'animal care', 'charm animal', 'heal',
                'lore (heraldry)', 'melee (cavalry)', 'ride (horse)', 'trade (farrier)'],
            ['cool', 'dodge', 'endurance', 'intimidate',
                'language (battle)', 'melee (any)'],
            ['charm', 'consume alcohol', 'leadership', 'lore (warfare)'],
            ['lore (any)', 'secret signs (knightly order)']
        ],
        'talents':
        [
            ['etiquette (any)', 'roughrider', 'sturdy', 'warrior born'],
            ['menacing', 'seasoned traveller', 'shieldsman', 'strike mighty blow'],
            ['fearless (any)', 'stout-hearted', 'unshakeable', 'warleader'],
            ['disarm', 'inspiring', 'iron will', 'strike to injure']
        ],
        'name': 'Knight',
        'class': 'Warrior',
        'trappings': [
            ['leather jack', 'mail shirt', 'riding horse with saddle and tack',
                'shield', 'trade tools (farrier)'],
            ['destrier with saddle and tack',
                'melee weapon (any)', 'lance', 'plate armour and helm'],
            ['barding', 'small units of knights'],
            ['plumed great helm', 'squire',
                'large unit of knights%several small units of knights']
        ]
    },

    ###

    'pit fighter': {
        'ranks': ['pugilist', 'pit fighter', 'pit champion', 'pit legend'],
        'status': ['brass 4', 'silver 2', 'silver 5', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 2, 3], [4], [5], [9]],
        'skills': [
            ['athletics', 'cool', 'dodge', 'endurance', 'gamble',
                'intimidate', 'melee (any)', 'melee (brawling)'],
            ['haggle', 'intuition',
                'melee (basic)', 'melee (flail)%melee (two-handed)', 'perception', 'ranged (entangling)'],
            ['consume alcohol', 'gossip', 'lore (anatomy)', 'perform (fight)'],
            ['charm', 'ranged (any)']
        ],
        'talents':
        [
            ['dirty fighter', 'in-fighter', 'iron jaw', 'reversal'],
            ['ambidextrous', 'combat reflexes', 'dual wielder', 'shieldsman'],
            ['combat master', 'disarm', 'menacing', 'robust'],
            ['frightening', 'furious assault', 'implacable', 'reaction strike']
        ],
        'name': 'Pit Fighter',
        'class': 'Warrior',
        'trappings': [
            ['bandages', 'knuckledusters', 'leather jack'],
            ['flail%great weapon', 'hand weapon', 'net%whip', 'shield%buckler'],
            ['breastplate', 'helmet'],
            ['quality helmet']
        ]
    },

    ###

    'protagonist': {
        'ranks': ['braggart', 'protagonist', 'hitman', 'assassin'],
        'status': ['brass 2', 'silver 1', 'silver 4', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 3, 5], [4], [1], [9]],
        'skills': [
            ['athletics', 'dodge', 'endurance',
                'entertain (taunt)', 'gossip', 'haggle', 'intimidate', 'melee (any)'],
            ['bribery', 'charm', 'intuition',
                'melee (basic)', 'perception', 'ride (horse)'],
            ['climb', 'cool', 'navigation', 'ranged (thrown)'],
            ['entertain (acting)', 'ranged (crossbow)']
        ],
        'talents':
        [
            ['in-fighter', 'dirty fighting', 'menacing', 'warrior born'],
            ['combat reflexes', 'criminal', 'reversal', 'strike to stun'],
            ['careful strike', 'disarm', 'marksman', 'relentless'],
            ['accurate shot', 'ambidextrous', 'furious assault', 'strike to injure']
        ],
        'name': 'Protagonist',
        'class': 'Warrior',
        'trappings': [
            ['hood%mask', 'knuckledusters', 'leather jack'],
            ['hand weapon', 'mail shirt',
                'riding horse with saddle and tack', 'shield'],
            ['cloak', 'garotte', 'poison', 'throwing knives'],
            ['crossbow with 10 shots', 'disguise kit']
        ]
    },

    ###

    'slayer': {
        'ranks': ['troll slayer', 'giant slayer', 'dragon slayer', 'daemon slayer'],
        'status': ['brass 2', 'brass 2', 'brass 2', 'brass 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 2, 8], [3], [5], [4]],
        'skills': [
            ['consume alcohol', 'cool', 'dodge', 'endurance',
                'gamble', 'heal', 'lore (trolls)', 'melee (basic)'],
            ['evaluate', 'intimidate',
                'language (battle)', 'lore (giants)', 'melee (two-handed)', 'outdoor survival'],
            ['entertain (storytelling)', 'lore (dragons)',
             'perception', 'ranged (thrown)'],
            ['intuition', 'lore (chaos)']
        ],
        'talents':
        [
            ['dual wielder', 'fearless (everything)', 'frenzy', 'slayer'],
            ['hardy', 'implacable', 'menacing', 'reversal'],
            ['ambidextrous', 'furious assault', 'relentless', 'robust'],
            ['combat master', 'frightening', 'strike mighty blow', 'very strong']
        ],
        'name': 'Slayer',
        'class': 'Warrior',
        'trappings': [
            ['axe', 'flask of spirits', 'shame', 'tattoos'],
            ['great axe', 'jewellery', "troll's head"],
            ["giant's head", 'throwing axes'],
            ["dragon's head"]
        ]
    },

    ###

    'soldier': {
        'ranks': ['recruit', 'soldier', 'sergeant', 'officer'],
        'status': ['silver 1', 'silver 3', 'silver 5', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 3, 8], [1], [4], [9]],
        'skills': [
            ['athletics', 'climb', 'cool', 'dodge', 'endurance',
                'language (battle)', 'melee (basic)', 'play (drum)%play (fife)'],
            ['consume alcohol', 'gamble', 'gossip',
                'melee (any)', 'ranged (any)', 'outdoor survival'],
            ['heal', 'intuition', 'leadership', 'perception'],
            ['lore (warfare)', 'navigation']
        ],
        'talents':
        [
            ['diceman', 'marksman', 'strong back', 'warrior born'],
            ['drilled', 'etiquette (soldiers)', 'rapid reload', 'shieldsman'],
            ['combat aware', 'enclosed fighter', 'unshakeable', 'warleader'],
            ['inspiring', 'public speaking', 'seasoned traveller', 'stout-hearted']
        ],
        'name': 'Soldier',
        'class': 'Warrior',
        'trappings': [
            ['dagger', 'leather breastplate', 'uniform'],
            ['breastplate', 'helmet', 'weapon (any)'],
            ['symbol of rank', 'unit of troops'],
            ['letter of commission', 'light warhorse with saddle and tack', 'map',
                'orders', 'unit of soldiers', 'quality uniform', 'symbol of rank']
        ]
    },

    ###

    'warrior priest': {
        'ranks': ['novitiate', 'warrior priest', 'priest sergeant', 'priest captain'],
        'status': ['brass 2', 'silver 2', 'silver 3', 'silver 4'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0, 3, 8], [2], [4], [9]],
        'skills': [
            ['cool', 'dodge', 'endurance', 'heal', 'leadership',
                'lore (theology)', 'melee (any)', 'pray'],
            ['charm', 'entertain (speeches)', 'intimidate',
             'language (battle)', 'melee (any)', 'ranged (any)'],
            ['animal care', 'intuition', 'perception', 'ride (horse)'],
            ['consume alcohol', 'lore (warfare)']
        ],
        'talents':
        [
            ['bless (any)', 'etiquette (cultists)',
             'read/write', 'strong-minded'],
            ['dual wielder', 'inspiring',
                'invoke (any)', 'seasoned traveller'],
            ['combat aware', 'holy visions', 'pure soul', 'stout-hearted'],
            ['fearless (any)', 'furious assault', 'holy hatred', 'warleader']
        ],
        'name': 'Warrior Priest',
        'class': 'Warrior',
        'trappings': [
            ['book (religion)', 'leather jerkin', 'religious symbol',
             'robes', 'weapon (any melee)'],
            ['breastplate', 'weapon (any)'],
            ['light warhorse with saddle and tack'],
            ['religious relic']
        ]
    },

    ###


}

final_career_list = {}

class_trappings = {
    'academic': ['clothing', 'dagger', 'pouch', 'sling bag', 'writing kit', '2°10|sheets of parchment'],
    'burgher': ['cloak', 'clothing', 'dagger', 'hat', 'pouch', 'sling', 'lunch'],
    'courtier': ['courtly garb', 'dagger', 'pouch', 'tweezers', 'ear pick', 'comb'],
    'peasant': ['cloak', 'clothing', 'dagger', 'pouch', 'sling bag', 'rations (1 day)'],
    'ranger': ['cloak', 'clothing', 'dagger', 'pouch', 'backpack', 'tinderbox', 'blanket', 'rations (1 day)'],
    'riverfolk': ['cloak', 'clothing', 'dagger', 'pouch', 'sling bag', 'flask of spirits'],
    'rogue': ['clothing', 'dagger', 'pouch', 'sling bag', '2 candles', '2°10|matches', 'hood%mask'],
    'warrior': ['clothing', 'hand weapon', 'dagger', 'pouch']

}

extra_careers= {

    'alchemist': {
        'ranks': ['alchemist apprentice', 'alchemist', 'master alchemist', 'alchemist lord'],
        'status': ['brass 4', 'silver 4', 'gold 3', 'gold 4'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3,7,8 ], [6], [4], [9]],
        'skills': [
            ['channeling (metal)','evaluate','haggle','intuition','language (magick)', 'lore (magic)', 'melee (basic)', 'melee (polearm)', 'perception','trade (alchemist)'],
            ['charm','cool','intimidate','lore (metallurgy)','research','trade (blacksmith)%trade (goldsmith)'],
            ['lore (engineering)', 'lore (science)', 'ride (horse)','trade (engineer)'],
            ['language (khazalid)', 'lore (any)']
        ],
        'talents':
        [
            ['aethyric attunement','petty magic','read/write','second sight'],
            ['arcane magic (metal)','argumentative','detect artefact','sixth sense'],
            ['bookish','craftsman (goldsmith)','instinctive diction','magical sense'],
            ['frightening','iron will','war wizard','wealth']
        ],
        'name': 'Alchemist',
        'class': 'Academic',
        'trappings': [
            ['grimoire','staff'],
            ['magical license','portable alchemical laboratory'],
            ['alchemist apprentice','light warhorse','magical item'],
            ['library (magic)%library (science)%library (engineering)','workshop (magic)%workshop (engineering)']
        ]
    
    },
        'astromancer': {
        'ranks': ['celestial acolyte', 'astromancer', 'grand astromancer', 'lord celestial'],
        'status': ['brass 4', 'silver 4', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,7,8], [5], [4], [9]],
        'skills': [
            ['augury','channeling (heavens)', 'dodge','entertain (fortune telling)', 'intuition','language (magick)', 'lore (magic)', 'melee (basic)', 'melee (polearm)', 'perception'],
            ['cool','gossip','intimidate','language (battle)', 'lore (astronomy)', 'research'],
            ['evaluate','navigation','lore (prophecy)', 'ride (horse)'],
            ['language (any)', 'lore (any)']
        ],
        'talents':
        [
            ['aethyric attunement','petty magic','read/write','second sight'],
            ['arcane magic (heavens)', 'detect artefact','orientation','sixth sense'],
            ['instinctive diction','magical sense','seasoned traveller','well-prepared'],
            ['frightening','iron will','night vision','war wizard']
        ],
        'name': 'Astromancer',
        'class': 'Academic',
        'trappings': [
            ['grimoire','staff',"starwatcher handbook"],
            ['ceremonial telescope','magical license','practical robes','sextant'],
            ['apprentice','expensive orrery%armillary sphere','light warhorse','magical item','standard robes'],
            ['elaborate robes','library (magic)','tower%mountaintop observatory']
        ]
    },

     'beadle': {
        'ranks': ['laboratory assistant', 'beadle', 'groundskeeper', 'terror of the faculty'],
        'status': ['silver 1', 'silver 2', 'silver 4', 'silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,7,8], [5], [4], [9]],
        'skills': [
            ['consume alcohol','dodge','endurance','gamble','gossip','intuition','melee (basic)','perception','stealth (urban)', 'trade (carpenter)'],
            ['athletics','charm','cool','intimidate','lore (any)','ranged (blackpowder)'],
            ['entertain (storytelling)','heal','melee (any)','track'],
            ['leadership','lore (any)']
        ],
        'talents':
        [
            ['diceman','read/write','savvy','warrior born'],
            ['carouser','etiquette (scholars)','reversal','strike mighty blow'],
            ['argumentative','fearless (intruders)','menacing','stout-hearted'],
            ['frightening','public speaker','suave','unshakeable']
        ],
        'name': 'Beadle',
        'class': 'Warrior',
        'trappings': [
            ['uniform in the colours of the faculty'],
            ['pistol%blunderbuss','12 shots','sleeved mail shirt'],
            ['helmet','master key to the faculty'],
            ['breastplate','crew of beadles']
        ]
    },
    'combat familiar': {
        'ranks': ['newly crafted','combat familiar','armoured mite','iron clad imp'],
        'status': ['brass 0', 'brass 0', 'brass 0', 'brass 0'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,2,4], [5], [6], [8]],
        'skills': [
            ['athletics','climb','cool','dodge','endurance','intuition','language (battle)', 'melee (any)', 'melee (any)',
             'perception'],
            ['intimidate','lore (warfare)','melee (any)','ride (horse)','stealth (rural)%stealth (urban)'],
            ['gamble','lore (heraldry)','melee (any)', 'stealth (rural)%stealth (urban)'],
            ['leadership','melee (any)']
        ],
        'talents':
        [
            ['ambidextrous','beat blade','distract','warrior born'],
            ['combat reflexes','implacable','riposte','very strong'],
            ['dual wielder','frenzy','furious assault','relentless'],
            ['combat master','strike mighty blow','strike to injure','strike to stun']
        ],
        'name': 'Combat Familiar',
        'class': 'Special',
        'trappings': [
            ['full plate armour','two weapons'],
            [],
            [],
            []
        ]
    },


      'druid': {
        'ranks': ["druid apprentice", 'druid', 'master druid', 'druid lord'],
        'status': ['brass 3', 'silver 3', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[5,7,8], [4], [9], [0]],
        'skills': [
            ['channeling (life)', 'charm animal','dodge','intuition','language (magick)','lore (magick)','melee (basic)', 'melee (polearm)', 'outdoor survival','perception'],
            ['charm','gossip','intimidate','language (battle)', 'language (any)', 'navigation'],
            ['animal care','evaluate','lore (plants)', 'ride (horse)'],
            ['language (any)', 'lore (any)']
        ],
        'talents':
        [
            ['aethyric attunement','petty magic','read/write','second sight'],
            ['arcane magic (life)', 'detect artefact','fast hands','sixth sense'],
            ['instinctive diction','magical sense','menacing','rover'],
            ['combat aware','frightening','iron will','war wizard']
        ],
        'name': 'Druid',
        'class': 'Academic',
        'trappings': [
            ['bronze sickle','grimoire','staff'],
            ['magical license','practical robes','silver sickle'],
            ['apprentice','gold sickle','magical item','standard robes'],
            ['elaborate robes','garden retreat','library (magic)']
        ]
    },

        'hierophant': {
        'ranks': ['acolyte of the light order', 'hierophant', 'master hierophant', 'guardian of the light order'],
        'status': ['brass 3', 'silver 3', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[4,7,8], [5], [0], [9]],
        'skills': [
            ['channeling (light)', 'dodge','entertain (singing)', 'intuition','language (magick)', 'lore (magic)', 'lore (nehekhara)', 'melee (basic)', 'melee (polearm)', 'perception'],
            ['charm','cool','gossip','language (any)', 'leadership','lore (warfare)'],
            ['evaluate','lore (daemonology)', 'research','ride (horse)'],
            ['language (any)', 'lore (any)']
        ],
        'talents':
        [
            ['aethyric attunement','petty magic','read/write','second sight'],
            ['arcane magic (light)', 'detect artefact','savvy','sixth sense'],
            ['dual wielder','instinctive diction','magical sense','tower of memories'],
            ['combat aware','iron will','menacing','resistance (chaos)']
        ],
        'name': 'Hierophant',
        'class': 'Academic',
        'trappings': [
            ['grimoire','staff','candle with holder'],
            ['magical license','practical robes'],
            ['acolyte apprentice','light warhorse','magical item','standard robes'],
            ['elaborate robes','library (magic)', 'study']
        ]
    },

    'magister vigilant': {
        'ranks': ['vigilant apprentice', 'magister vigilant', 'magister inquisitor', 'lord vigilant'],
        'status': ['brass 4', 'silver 4', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,7,8], [5], [4], [2]],
        'skills': [
            ['channeling (any)','charm','cool','dodge','intuition','language (magick)', 'lore (magic)', 'melee (basic)', 'melee (polearm)', 'perception'],
            ['charm','gossip','intimidate','language (battle)','pick lock','research'],
            ['navigation','secret signs (any)','sleight of hand','stealth (urban)'],
            ['lore (any)', 'set trap']
        ],
        'talents':
        [
            ['blather','petty magic','read/write','savvy'],
            ['arcane magic (any)', 'fast hands','menacing','shadow'],
            ['break and enter','magical sense','second sight','sixth sense'],
            ['alley cat','frightening','iron will','nose for trouble']
        ],
        'name': 'Magister Vigilant',
        'class': 'Academic',
        'trappings': [
            ['disguise','grimoire'],
            ['magical license'],
            ['magical item'],
            ['standard robes']
        ]
    },

    'mundane alchemist': {
        'ranks': ['tinkerer', 'alchemist', 'master alchemist', 'transmutator'],
        'status': ['brass 3', 'silver 2', 'silver 3', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[3,6,7], [4], [8], [5]],
        'skills': [
            ['charm','consume alcohol','gossip','haggle','language (classical)','lore (chemistry)', 'lore (geology)', 'lore (science)', 'trade (alchemist)', 'trade (poisoner)'],
            ['intuition','lore (medicine)', 'language (guilder)', 'perception','research','secret signs (guilder)'],
            ['drive','language (any)', 'leadership','lore (any)'],
            ['channeling (metal)', 'ride (horse)']
        ],
        'talents':
        [
            ['concoct','crafstman (alchemist)', 'read/write', 'savvy'],
            ['criminal','etiquette (guilder)','magical sense','nimble fingered'],
            ['bookish','detect artefact','master tradesman (alchemist)','petty magic'],
            ['arcane magic (metal)', 'master tradesman (poisoner)', 'resistance (poison)', 'savant (alchemy)']
        ],
        'name': 'Mundane Alchemist',
        'class': 'Academic',
        'trappings': [
            ['book (blank)', 'leather jerkin','pestle and mortar','tripod','test tubes and alembic','writing kit'],
            ['guild license','trade tools'],
            ['apprentice','book (alchemy)', 'laboratory'],
            ['fine quality laboratory','letter of commission']
        ]
    },
    'pyromancer': {
        'ranks': ['apprentice pyromancer', 'pyromancer', 'master pyromancer', 'pyromancer lord'],
        'status': ['brass 3', 'silver 3', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,7,8], [5], [4], [9]],
        'skills': [
            ['channeling (fire)', 'dodge','intimidate','intuition','language (battle)', 'language (magick)', 'lore (magic)','melee (basic)', 'melee (polearm)', 'perception'],
            ['charm','cool','gossip','language (any)', 'leadership','lore (warfare)'],
            ['animal care','evaluate','research','ride (horse)'],
            ['language (any)', 'lore (any)']
        ],
        'talents':
        [
            ['aethyric attunement','petty magic','read/write','second sight'],
            ['arcane magic (fire)','detect artefact','fast hands','sixth sense'],
            ['dual wielder','instinctive diction','magical sense','menacing'],
            ['combat aware','frightening','iron will','war wizard']
        ],
        'name': 'Pyromancer',
        'class': 'Academic',
        'trappings': [
            ['first key of secrets','grimoire','staff'],
            ['magical license','practical robes','second key of secrets','third key of secrets','sword'],
            ['apprentice','fourt key of secrets','fifth key of secrets','light warhorse','magical item','standard robes'],
            ['apprentice','elaborate robes','library (magic)','sixth key of secrets','seventh key of secrets','workshop (magic)']
        ]
    },

        'scryer': {
        'ranks': ['haunted', 'scryer', 'psychometrician', 'reader of the past'],
        'status': ['brass 1', 'brass 3', 'silver 2', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[7,8,9], [4], [5], [6]],
        'skills': [
            ['dodge','intuition','lore (local)', 'melee (basic)', 'outdoor survival','navigation','perception','psychometry','sleight of hand','stealth (rural)'],
            ['bribery','cool','endurance','gossip','haggle','intimidate'],
            ['charm','evaluate','lore (history)','lore (politics)'],
            ['entertain (storytelling)', 'leadership']
        ],
        'talents':
        [
            ['beneath notice','luck','orientation','second sight'],
            ['coolheaded','criminal','savvy','sixth sense'],
            ['etiquette (nobles)', 'menacing','nose for trouble','well-prepared'],
            ['commanding presence','frightening','magical sense','strong-minded']
        ],
        'name': 'Scryer',
        'class': 'Peasant',
        'trappings': [
            ['backpack with tent','dagger','practical outdoor clothing'],
            ['permanent abode'],
            ['respectable clothing'],
            ['fine clothing','town house']
        ]
    },
    'shadowmancer': {
        'ranks': ['trickster apprentice', 'shadowmancer', 'grey guardian', 'grey lord'],
        'status': ['brass 3', 'silver 3', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[5,7,8], [4], [0], [6]],
        'skills': [
            ['channeling (shadow)','dodge','intuition','language (battle)','language (magic)','lore (magic)','melee (basic)','melee (polearm)','perception','secret signs (grey order)'],
            ['charm','cool','gossip','intimidate','language (any)','leadership'],
            ['evaluate','lore (politics)','research','ride (horse)'],
            ['language (any)', 'lore (any)']
        ],
        'talents':
        [
            ['aethyric attunement','petty magic','read/write','second sight'],
            ['arcane magic (shadow)','detect artefact','fast hands','sixth sense'],
            ['blather','instinctive diction','magical sense','mimic'],
            ['secret identity','shadow','tower of memories','war wizard']
        ],
        'name': 'Shadowmancer',
        'class': 'Academic',
        'trappings': [
            ['grimoire','hooded cloak','staff'],
            ['magical license'],
            ['apprentice','light warhorse','magical item'],
            ['apprentice','library (magic)','ring of informers','workshop (magic)']
        ]
    },

        'shaman': {
        'ranks': ['shaman apprentice', 'amber wizard', 'master shaman', 'shaman lord'],
        'status':  ['brass 3', 'silver 3', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,7,8], [5], [4], [3]],
        'skills': [
            ['animal care','channeling (beasts)','cool','dodge','intuition','language (magick)','lore (magic)','melee (polearm)','outdoor survival','perception'],
            ['animal training','charm animal','intimidate','ranged (bow)','stealth (rural)','track'],
            ['evaluate','navigation','research','ride (horse)'],
            ['lore (any)','leadership']
        ],
        'talents':
        [
            ['aethyric attunement','petty magic','read/write','second sight'],
            ['arcane magic (beasts)','coolheaded','fast hands','sixth sense'],
            ['animal affinity','instinctive diction','magical sense','menacing'],
            ['frightening','iron will','lightning reflexes','war wizard']
        ],
        'name': 'Shaman',
        'class': 'Academic',
        'trappings': [
            ['staff'],
            ['magical license'],
            ['apprentice','magical item'],
            ['conclave of shamans','shamanic lair']
        ]
    },
        'spell familiar': {
        'ranks': ['newly conjured', 'spell familiar', 'mystery imp', 'wizardling'],
        'status': ['brass 0', 'brass 0', 'brass 0', 'brass 0'],
        #first three are on level 1, then level 2 and so on
        'stats': [[6,7,8], [4], [5], [9]],
        'skills': [
            ['channeling (any)','cool','dodge','gossip','intuition','language (magick)','lore (magic)','melee (basic)','perception','stealth (rural)%stealth (urban)'],
            ['charm','language (any)','lore (any)', 'melee (polearm)','research','ride (horse)'],
            ['evaluate','language (any)', 'lore (any)', 'sleight of hand'],
            ['language (any)','lore (any)']
        ],
        'talents':
        [
            ['aethyric attunement','coolheaded','savvy','second sight'],
            ['arcane magic (any)','instinctive diction','luck','sixth sense'],
            ['bookish','detect artefact','nose for trouble','perfect pitch'],
            ['fast hands','frightening','war wizard','witch!']
        ],
        'name': 'Spell Familiar',
        'class': 'Special',
        'trappings': [
            ['grimoire','dagger'],
            [],
            [],
            []
        ]
    },

        'spiriter': {
        'ranks': ['apprentice', 'amethyst wizard', 'master spiriter', 'magister lord'],
        'status': ['brass 2', 'silver 3', 'gold 1', 'gold 2'],
        #first three are on level 1, then level 2 and so on
        'stats': [[6,7,8], [5], [4], [3]],
        'skills': [
            ['channeling (death)','cool','dodge','intimidate','intuition','language (magick)','lore (magic)','melee (basic)','melee (polearm)','perception'],
            ['art (engraving)','endurance','evaluate','language (battle)', 'lore (undead)','research'],
            ['animal care','leadership','lore (warfare)','ride (horse)'],
            ['language (any)','lore (any)']
        ],
        'talents':
        [
            ['aethyric attunement','petty magic','read/write','second sight'],
            ['arcane magic (death)','detect artefact','fast hands','sixth sense'],
            ['instinctive diction','magical sense','menacing','resistance (poison)%resistance (disease)'],
            ['combat aware','frightening','iron will','war wizard']
        ],
        'name': 'Spiriter',
        'class': 'Academic',
        'trappings': [
            ['grimoire','staff of petrified wood'],
            ['magical licence','scythe'],
            ['apprentice','light warhorse','magical item'],
            ['library (magic)','workshop (magic)']
        ]
    },


     'archer': {
        'ranks': ['bowman', 'archer', 'archer sergeant', 'archer captain'],
        'status': ['silver 1', 'silver 3', 'silver 5', 'gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,3,4],[2],[3],[7]],
        'skills': [
            ['athletics','climb','consume alcohol','dodge','endurance','language (battle)','perception',
             'play (horn)','ranged (bow)','stealth (rural)'],
            ['gamble','gossip','melee (basic)','outdoor survival','track','trade (fletcher)'],
            ['cool','leadership','navigation','ride (horse)'],
            ['lore (warfare)','secret signs (scout)']
        ],
        'talents':
        [
            ['accurate shot','fast shot','strong back','warrior born'],
            ['drilled','etiquette (soldiers)','marksman','sure shot'],
            ['combat aware','sharpshooter','sniper','unshakeable'],
            ['inspiring','seasoned traveller','stout-hearted','warleader']
        ],
        'name': 'Archer',
        'class': 'Warrior',
        'trappings': [
            ['quiver','10 arrows','bow','dagger','pack','uniform'],
            ['headgear','sword','quality bow'],
            ['symbol of rank','quality uniform'],
            ['letter of commission','light warhorse with saddle and tack']
        ]
    },


    'artillerist': {
        'ranks': ['apprentice artillerist','artillerist','artillerist captain','master artillerist'],
        'status': ['silver 1','silver 3','silver 5','gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[1,4,7],[3],[8],[5]],
        'skills': [
            ['animal care','cool','drive','endurance','evaluate','language (battle)','melee (basic)',
             'navigation','perception','ranged (blackpowder)%ranged (catapult)%ranged (crossbow)%ranged (engineering)'],
            ['consume alcohol','gamble','gossip','outdoor survival','ranged (blackpowder)%ranged (catapult)%ranged (crossbow)%ranged (engineering)',
             'trade (carpenter)%trade (gunsmith)'],
            ['intuition','leadership','lore (artillery)','ride (horse)'],
            ['charm','lore (warfare)']
        ],
        'talents':
        [
            ['marksman','rapid reload','strong back','warrior born'],
            ['crew commander','etiquette (soldiers)','orientation','sniper'],
            ['combat aware','read/write','tinker','unshakeable'],
            ['inspiring','public speaking','seasoned traveller','stout-hearted']
        ],
        'name': 'Artillerist',
        'class': 'Academic',
        'trappings': [
            ['dagger','leather apron'],
            ['weapon (any)','telescope','tools','uniform'],
            ['symbol of rank','quality uniform'],
            ['artillery piece and limber','letter of commission','light warhorse with saddle and tack','map']
        ]
    },

    'camp follower': {
        'ranks': ['ribaud','camp follower','seasoned scavenger','camp chief'],
        'status': ['brass 1','brass 4','silver 1','silver 4'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,5,9],[7],[4],[3]],
        'skills': [
            ['charm','consume alcohol','dodge','entertain (any)','gossip','haggle','melee (any)','outdoor survival',
             'perception','perform (dance)'],
            ['athletics','bribery','endurance','gamble','ranged (any)','stealth (rural)'],
            ['cool','intimidate','intuition','language (any)'],
            ['evaluate','leadership']
        ],
        'talents':
        [
            ['attractive','beneath notice','blather','dirty fighting'],
            ['diceman','etiquette (soldiers)','rover','stone soup'],
            ['seasoned traveller','sturdy','unshakeable','very resilient'],
            ['inspiring','public speaking','stout-hearted','strong-minded']
        ],
        'name': 'Camp Follower',
        'class': 'Ranger',
        'trappings': [
            ['bed roll','dagger','pack'],
            ['tent','quality hat'],
            ['quality clothing'],
            ['riding horse with saddle and tack','ring of camp followers']
        ]
    },

    'cartographer': {
        'ranks': ['surveyor','cartographer','chartered cartographer','master cartographer'],
        'status': ['silver 1','silver 3','silver 5','gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[4,6,7],[0],[5],[8]],
        'skills': [
            ['art (cartography)','climb','evaluate','lore (geography)','melee (basic)','navigation',
             'outdoor survival','perception','ride (horse)','stealth (rural)'],
            ['charm','endurance','gossip','haggle','lore (heraldry)','trade (cartographer)'],
            ['intuition','language (guilder)','research','secret signs (guilder)'],
            ['language (any)','lore (any)']
        ],
        'talents':
        [
            ['artistic','orientation','read/write','rover'],
            ['bookish','coolheaded','flee!','strider (any)'],
            ['seasoned traveller','etiquette (guilders)','nimble-fingered','unshakeable'],
            ['dealmaker','stout-hearted','master tradesman (cartographer)','magnum opus']
        ],
        'name': 'Cartographer',
        'class': 'Academic',
        'trappings': [
            ['vellum','writing kit'],
            ['horse with saddle and tack','theodolite'],
            ['letter of charter','quality travel clothes'],           
            ['study','quality theodolite']
        ]
    },

'freelance': {
        'ranks': ['squire','freelance knight','freelance captain','knight commander'],
        'status': ['silver 1','silver 2','gold 1','gold 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2,4,5],[0],[8],[9]],
        'skills': [
            ['athletics','animal care','charm animal','consume alcohol','heal','gossip','melee (cavalry)',
             'outdoor survival','ride (horse)','trade (farrier)'],
            ['charm','cool','dodge','endurance','intimidate','intuition','melee (any)'],
            ['haggle','gamble','leadership','lore (warfare)'],
            ['language (battle)','lore (any)']
        ],
        'talents':
        [
            ['roughrider','sturdy','warrior born','combat aware'],
            ['etiquette (any)','seasoned traveller','strike mighty blow','stone soup'],
            ['combat master','stout-hearted','unshakeable','warleader'],
            ['luck','disarm','iron will','inspiring']
        ],
        'name': 'Freelance',
        'class': 'Warrior',
        'trappings': [
            ['leather jack','mail shirt','riding horse with saddle and tack','shield','trade tools (farrier)'],
            ['destrier with saddle and tack','melee weapon (any)','plate armour and helm','personal heraldry'],
            ['barding','small retinue of followers'],
            ['company of knights','squire']
        ]
    },

    'greatsword': {
        'ranks': ['greatsword cadet','greatsword','greatsword sergeant','greatsword captain'],
        'status': ['silver 1','silver 3','silver 5','gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,2,8],[4],[3],[7]],
        'skills': [
            ['athletics','consume alcohol','cool','dodge','endurance','gossip','language (battle)',
             'melee (basic)','melee (two-handed)','play (drum)'],
            ['gamble','intimidate','lore (heraldry)','melee (any)','outdoor survival','perception'],
            ['intuition','leadership','navigation','ride (horse)'],
            ['charm','lore (warfare)']
        ],
        'talents':
        [
            ['coolheaded','drilled','strong back','warrior born'],
            ['combat reflexes','etiquette (soldiers)','fearless (any)','strike mighty blow'],
            ['combat aware','enclosed fighter','unshakeable','warleader'],
            ['commanding presence','inspiring','public speaking','stout-hearted']
        ],
        'name': 'Greatsword',
        'class': 'Warrior',
        'trappings': [
            ['dagger','metal breastplate','uniform','zweihänder'],
            ['full plate armour','large feathered hat'],
            ['manual on the art of zweihänder fighting','quality zweihänder','symbol of rank'],
            ['letter of commission','light warhorse with saddle and tack']
        ]
    },

     'halberdier': {
        'ranks': ['halberdier recruit','halberdier','halberdier sergeant','halberdier captain'],
        'status': ['silver 1','silver 3','silver 5','gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,3,5],[2],[4],[7]],
        'skills': [
            ['athletics','consume alcohol','dodge','endurance','language (battle)','melee (basic)',
             'melee (polearm)','perform (parade)','play (drum)'],
            ['climb','gamble','gossip','intimidate','outdoor survival','perception'],
            ['intuition','leadership','navigation','ride (horse)'],
            ['charm','lore (warfare)']
        ],
        'talents':
        [
            ['diceman','drilled','strong back','warrior born'],
            ['enclosed fighter','etiquette (soldier)','fearless (any)','strike mighty blow'],
            ['combat aware','unshakeable','stout-hearted','warleader'],
            ['inspiring','public speaking','seasoned traveller','commanding presence']
        ],
        'name': 'Halberdier',
        'class': 'Warrior',
        'trappings': [
            ['dagger','halberd','leather breastplate','uniform'],
            ['metal breastplate','helmet','quality halberd'],
            ['symbol of rank','quality uniform'],
            ['letter of commission','light warhorse with saddle and tack','quality sword']
        ]
    },


        'handgunner': {
        'ranks': ['handgunner recruit','handgunner','handgunner sergeant','handgunner captain'],
        'status': ['silver 1','silver 3','silver 5','gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[1,5,6],[4],[7],[8]],
        'skills': [
            ['athletics','consume alcohol','cool','dodge','endurance','language (battle)','melee (basic)','perception',
             'play (flute)','ranged (blackpowder)'],
            ['climb','gamble','gossip','intuition','outdoor survival','trade (gunsmith)'],
            ['leadership','navigation','ranged (engineer)','ride (horse)'],
            ['charm','lore (warfare)']
        ],
        'talents':
        [
            ['accurate shot','gunner','marksman','sniper'],
            ['drilled','etiquette (soldiers)','fast shot','rapid reload'],
            ['combat aware','sharpshooter','sure shot','unshakeable'],
            ['inspiring','seasoned traveller','stout-hearted','warleader']
        ],
        'name': 'Handgunner',
        'class': 'Warrior',
        'trappings': [
            ['dagger','handgun','uniform'],
            ['large feathered hat','quality handgun'],
            ['symbol of rank','quality uniform'],
            ['letter of commission','light warhorse with saddle and tack']
        ]
    },

    'knight panther': {
        'ranks': ['squire','knight','first knight','company commander (inner circle)'],
        'status': ['silver 3','silver 5','gold 2','gold 4'],
        #first three are on level 1, then level 2 and so on
        'stats': [[2,4,5],[0],[8],[9]],
        'skills': [
            ['athletics','animal care','charm animal','heal','lore (empire)','lore (heraldry)','melee (basic)','melee (cavalry)',
             'ride (horse)','trade (farrier)'],
            ['cool','dodge','endurance','intimidate','language (battle)','melee (any)'],
            ['charm','language (any)','leadership','lore (warfare)'],
            ['secret signs (knights panther)','lore (any)']
        ],
        'talents':
        [
            ['etiquette (any)','roughrider','sturdy','warrior born'],
            ['menacing','shieldsman','strike mighty blow','coolheaded'],
            ['fearless (chaos)','stout-hearted','unshakeable','warleader'],
            ['disarm','inspiring','iron will','strike to injure']
        ],
        'name': 'Knight Panther',
        'class': 'Warrior',
        'trappings': [
            ['leather jack','mail shirt','riding horse with saddle and tack','shield','trade tools (farrier)'],
            ['great cat pelt','destrier with saddle and tack','melee weapon (sword)','lance','plate armour and great helm with bestial crest',
             'ring with panther emblem%medallion with panther emblem'],
            ['barding','small unit of knights panther'],
            ['squire','large unit of knights panther%several small units of knights']
        ]
    },

    'knight of the blazing sun': {
        'ranks': ['novice','knight','hochmeister','knight of the inner circle'],
        'status': ['silver 3','silver 5','gold 2','gold 4'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,2,4],[7],[5],[9]],
        'skills': [
            ['athletics','animal care','charm animal','heal','language (classical)','lore (heraldry)','lore (any)',
             'melee (basic)','melee (cavalry)','ride (horse)'],
            ['cool','dodge','endurance','intimidate','language (battle)','melee (any)','lore (warfare)'],
            ['charm','ranged (any)','leadership','research'],
            ['secret signs (blazing sun)','lore (any)']
        ],
        'talents':
        [
            ['etiquette (any)','read/write','roughrider','warrior born'],
            ['seasoned traveller','savvy','shieldsman','strike to injure'],
            ['fearless (any)','warleader','disarm','unshakeable'],
            ['inspiring','stout-hearted','wealthy','strike mighty blow']
        ],
        'name': 'Knight of the Blazing Sun',
        'class': 'Warrior',
        'trappings': [
            ['leather jack','mail shirt','riding short with saddle and tack','shield','trade tools (farrier)','religious symbol (myrmidia)'],
            ['destrier with saddle and tack','melee weapon (any)','lance','plate armour and helm'],
            ['barding','small unit of blazing sun knights'],
            ['great helm with sun emblem','squire','large unit of knights%several small units of knights']
        ]
    },

    'knight of the white wolf': {
        'ranks': ['novice','knight','templar sergeant','company commander (inner circle)'],
        'status': ['silver 3','silver 5','gold 2','gold 3'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,2,4],[5],[8],[3]],
        'skills': [
            ['athletics','animal care','charm animal','heal','lore (heraldry)','melee (basic)','melee (cavalry)',
             'outdoor survival','ride (horse)','trade (farrier)'],
            ['cool','dodge','endurance','intimidate','language (battle)','melee (any)'],
            ['consume alcohol','leadership','lore (warfare)','perception'],
            ['lore (any)','secret signs (ulric)']
        ],
        'talents':
        [
            ['roughrider','sturdy','warrior born','hardy'],
            ['strike mighty blow','menacing','intimidate','seasoned traveller'],
            ['furious assault','unshakeable','fearless (any)','warleader'],
            ['iron will','inspiring','cool-headed','implacable']
        ],
        'name': 'Knight of the White Wolf',
        'class': 'Warrior',
        'trappings': [
            ['leather jack','mail shirt','riding horse with saddle and tack','cavalry hammer','trade tools (farrier)',
             'religious symbol (ulric)'],
            ['destrier with saddle and tack','plate armour','wolfskin cloak'],
            ['barding','small unit of white wolf knights'],
            ['novice','company of white wolf knights']
        ]
    },

'light cavalry': {
        'ranks': ['reiver','light cavalry','lance','captain'],
        'status': ['brass 3','silver 2','silver 5','gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,3,5],[1],[9],[7]],
        'skills': [
            ['animal care','dodge','endurance','haggle','heal','language (battle)','melee (basic)','outdoor survival',
             'ranged (throwing)','ride (horse)'],
            ['consume alcohol','etiquette (mercenaries)','gamble','gossip','melee (cavalry)','ranged (bow)'],
            ['drive','intuition','leadership','lore (warfare)'],
            ['lore (law)%lore (heraldry)','ranged (blackpowder)']
        ],
        'talents':
        [
            ['diceman','field dressing','flee!','strong back'],
            ['combat aware','orientation','rover','rough rider'],
            ['combat reflexes','rapid reload','seasoned traveller','trick riding'],
            ['commanding presence','dealmaker','inspiring','war leader']
        ],
        'name': 'Light Cavalry',
        'class': 'Warrior',
        'trappings': [
            ['shield%buckler','hand weapon','leather jack','riding horse with saddle and tack','javelin'],
            ['hand weapon','light warhorse','mail coat','open helm','shield'],
            ['lance','mail chausses','squire','page'],
            ['brace of pistols with gunpowder and ammunition','warhorse','flamboyant clothing','breastplate']
        ]
    },

    'pikeman': {
        'ranks': ['recruit','pikeman','file leader','banner captain'],
        'status': ['brass 5','silver 1','silver 4','gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,2,3],[8],[5],[9]],
        'skills': [
            ['athletics','climb','consume alcohol','dodge','endurance','gamble','language (battle)','language (tilean)',
             'melee (basic)','melee (polearm)'],
            ['cool','gossip','heal','intimidate','lore (warfare)','outdoor survival'],
            ['haggle','intuition','leadership','perception'],
            ['lore (law)','ride (horse)']
        ],
        'talents':
        [
            ['drilled','reaction strike','very strong','warrior born'],
            ['diceman','enclosed fighter','etiquette (mercenaries)','fearless (cavalry)'],
            ['combat aware','combat reflexes','field dressing','robust'],
            ['inspiring','unshakeable','very resilient','war leader']
        ],
        'name': 'Pikeman',
        'class': 'Warrior',
        'trappings': [
            ['hand weapon','leather breastplate','leather skullcap','pike','uniform in unit colours'],
            ['dice','mail coat','open helm'],
            ['plate breastplate','sash of rank'],
            ['baton of rank','banner-bearer','light warhorse','quality uniform','place bracers and leggings',
             'phalanx of pikemen','unit banner']
        ]
    },

  'priest of myrmidia': {
        'ranks': ['first eagle','warrior priest','priest sergeant','sergeant captain'],
        'status': ['silver 2','silver 3','silver 4','silver 5'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,4,5],[7],[2],[8]],
        'skills': [
            ['cool','dodge','language (battle)','leadership','lore (warfare)','lore (theology)','melee (basic)',
             'melee (polearm)','perception','pray'],
            ['charm','entertain (speeches)','heal','intuition','melee (any)','ranged (any)'],
            ['lore (warfare)','melee (any)','research','trade (weaponsmith)%trade (armoursmith)'],
            ['animal care','ride (horse)']
        ],
        'talents':
        [
            ['bless (myrmidia)','etiquette (cultists)','read/write','bookish'],
            ['drilled','inspiring','invoke (myrmidia)','shieldsman'],
            ['combat aware','holy visions','pure soul','stout-hearted'],
            ['combat master','combat reflexes','fearless (any)','warleader']
        ],
        'name': 'Warrior Priest of Myrmidia',
        'class': 'Warrior',
        'trappings': [
            ['myrmidian holy book','leather jerkin','myrmidian icon','white robes','spear'],
            ['breastplate and helmet','shield'],
            ['full plate armour'],
            ['religious relic (myrmidian)']
        ]
    },

    'siege specialist': {
        'ranks': ['crossbowman','siege specialist','sapper','siege master'],
        'status': ['silver 1','silver 3','silver 5','gold 1'],
        #first three are on level 1, then level 2 and so on
        'stats': [[0,1,2],[5],[7],[9]],
        'skills': [
            ['athletics','climb','consume alcohol','endurance','gamble','gossip','language (battle)','melee (basic)',
             'outdoor survival','ranged (crossbow)'],
            ['intuition','lore (engineering)','melee (two-handed)','perception','set trap','trade (miner)'],
            ['leadership','ranged (blackpowder)','ranged (engineering)','trade (explosives)'],
            ['haggle','lore (law)','ride (horse)']
        ],
        'talents':
        [
            ['etiquette (mercenaries)','marksman','rapid reload','strong back'],
            ['enclosed fighter','hardy','orientation','tunnel rat'],
            ['accurate shot','craftsman (explosives)','gunner','unshakeable'],
            ['combat aware','master tradesman (engineering)','savvy','war leader']
        ],
        'name': 'Siege Specialist',
        'class': 'Warrior',
        'trappings': [
            ['crossbow and ammunition','hand weapon','pavise','leather jack and skullcap','feathered hat'],
            ['two-handed pick','shovel'],
            ['book of ballistics tables','set of six sixty-second fuses','plate breastplate','pistol with bullets and ammunition',
             'trade tools (engineering)'],
            ['quality clothes','light warhorse','pavilion tent','body servant']
        ]
    }    


}

'''
    '': {
        'ranks': ['','','',''],
        'status': ['','','',''],
        #first three are on level 1, then level 2 and so on
        'stats': [[,,],[],[],[]],
        'skills': [
            [],
            [],
            [],
            []
        ],
        'talents':
        [
            [],
            [],
            [],
            []
        ],
        'name': '',
        'class': '',
        'trappings': [
            [],
            [],
            [],
            []
        ]
    }
'''