
arcane_spells = {
    'petty': ['Animal Friend', 'Bearings', 'Dazzle', 'Careful Step', 'Conserve', 'Dart', 'Drain', 'Eavesdrop', 'Gust', 'Light', 'Magic Flame', 'Marsh Lights', 'Murmured Whisper',
               'Produce Small Animal', 'Protection From Rain', 'Purify Water', 'Rot', 'Sleep', 'Spring', 'Shock', 'Sly Hands', 'Sounds', 'Twitch', 'Warning'],

    'arcane': ['Aethyric Armour','Aethyric Arms','Arrow Shield','Blast','Bolt','Breath','Bridge','Chain Attack','Corrosive Blood','Dark Vision','Distracting','Dome','Drop',
               'Entangle','Fearsome','Flight','Magic Shield','Move Object','Mundane Aura','Push','Teleport','Terrifying','Ward'],

    'winds':
    {
        'beasts': ['Amber Talons','Beast Form','Beast Master','Beast Tongue','Flock of Doom',"Hunter's Hide",'The Amber Spear',"Wyssan's Wildform"],
        'death': ['Caress of Laniph','Dying Words','Purple Pall of Shyish','Sanctify','Scythe of Shyish','Soul Vortex','Steal Life','Swift Passing'],
        'fire' : ["Aqshy's Aegis",'Cauterise','Crown of Flame','Flaming Hearts','Firewall',"Great Fires of U'zhul",'Flaming Sword of Rhuin','Purge'],
        'hedge': ['Goodwill','Mirkride','Nepenthe','Nostrum','Part the Branches','Protective Charm'],
        'heavens' : ['Cerulean Shield','Comet of Casandora',"Fate's Fickle Fingers",'Starcrossed',"T'essla's Arc",'The First Portent of Amul','The Second Portent of Amul',
                     'The Third Portent of Amul'],
        'life' : ['Barkskin','Earthblood','Earthpool','Fat of the Land','Forest of Thorns','Lie of the Land','Lifebloom','Regenerate'],
        'light' : ['Banishment','Blinding Light','Clarity of Thought','Daemonbane','Healing Light','Net of Amyntok',"Phâ's Protection",'Speed of Thought'],
        'metal' : ['Crucible of Chamon','Enchant Weapon','Feather of Lead',"Fool's Gold",'Forge of Chamon','Glittering Robe','Mutable Metal','Transmutation of Chamon'],
        'shadow' : ['Choking Shadows','Doppelganger','Illusion','Mindslip','Mystifying Miasma','Shadowsteed','Shadowstep','Shroud of Invisibility'],
        'witchcraft': ['Blight','Creeping Menace','Curse of Crippling Pain','Curse of Ill-Fortune','Haunting Horror','The Evil Eye'],
    },

    'witch':
    {
    },

    'dark':
    {
        'chaos': ['Blast of Corruption','Bolt of Corruption','Daemonic Mien','Destroy Lesser Daemon','Detect Daemon','Foul Messenger','Joyous Aspect','Manifest Lesser Daemon','Obsession','Octagram','Power of Chaos','Rend Aethyr','Slave to Darkness'],
        'necromancy': ['Raise Dead','Reanimate','Screaming Skull',"Vanhel's Call"],
        'nurgle': ['Bless with Filth','Cloud of Corruption','Mantle of Contagion','Pestilent Breath','Poisonous Pustule','Putrefy','Stream of Corruption','Toxic Rain','Veil of Flies','Weeping Wound','Wither'],
        'slaanesh': ['Acquiescence','Aura of Acquiescence','Bonds of Slaanesh','Breath of Inspiration',
                     'Blissful Throes','Cacophonic Caress','Careless Whispers','Chaos Spawn','Cursed Caress',
                     'Cutting Wit','Delicious Excruciation','Fleshy Curse','Flesh Puppet','From Pain, Pleasure','Lash of Slaanesh',
                     'Gift of Slaanesh','Luxurious Torment','Mask of Desire','Pavane of slaanesh','Phantasmagoria',"Succubus's Caress",'Summon Daemonette',
                     'Summon Daemonetter Pack','Titillating Delusions'],
        'tzeentch': ['Bension of Tzeentch','Bolt of Change','Boon of Tzeentch','Bestial Rage','Blue Fire of Tzeentch','Climb','Curse of Tzeentch',
                     'Enrage Beast','Gift of the Beast','Master of Fortune','Mindfire','Pink Fire of Tzeentch','Sense the Skein','Slave to Chaos',
                     'Subvert Strength','The Flickering Flames of Fickle Fate','The Purple Hand','Transformation of the Beast','Transformation of Tzeentch',
                     'Treason of Tzeentch','Tremor',"Tzeentch's Firestorm","Tzeentch's Golden Aura",'Word of Tzeentch']
    }
}

final_arcane_spells = {}

blessings = {
    'manann': ['Battle','Breath','Courage','Hardiness','Savagery','Tenacity'],
    'morr': ['Breath','Courage','Fortune','Righteousness','Tenacity','Wisdom'],
    'myrmidia': ['Battle','Conscience','Courage','Fortune','Protection','Righteousness'],
    'ranald': ['charisma','Conscience','Finesse','Fortune','Protection','Wit'],
    'rhya': ['Breath','Conscience','Grace','Healing','Protection','recuperation'],
    'shallya': ['Breath','Conscience','Healing','Protection','recuperation','Tenacity'],
    'sigmar': ['Battle','Courage','Hardiness','Might','Protection','Righteousness'],
    'taal': ['Battle','Breath','Conscience','Hardiness','The Hunt','Savagery'],
    'ulric': ['Battle','Courage','Hardiness','Might','Savagery','Tenacity'],
    'verena': ['Conscience','Courage','Fortune','Righteousness','Wisdom','Wit']
}

miracles = {
    'manann': ['Becalm','Fair Winds',"Drowned Man's Face","Manann's Bounty",'Sea Legs','Waterwalk'],
    'morr': ['Death Mask','Destroy Undead','Dooming','Last Rites',"Portal's Threshold","Stay Morr's Hand"],
    'myrmidia': ['Blazing Sun',"Eagle's Eye","Fury's Call",'Inspiring','Shield of Myrmidia','Spear of Myrmidia'],
    'ranald': ['An Invitation',"Cat's Eyes","Ranald's Grace",'Rich Man, Poor Man, Beggar Man, Thief','Stay Lucky',"You ain't seen me, right?"],
    'rhya': ["Rhya's Children","Rhya's Harvest","Rhya's Shelter","Rhya's Succour","Rhya's Touch","Rhya's Union"],
    'shallya': ["Anchorite's Endurance","Balm to a Wounded Mind",'Bitter Catharsis','Martyr',"Shallya's Tears",'Unblemished Innocence'],
    'sigmar': ['Beacon of Righteous Virtue','Heed Not the Witch',"Sigmar's Fiery Hammer",'Soulfire','Twin-tailed Comet','Vanquish the Unrighteous'],
    'taal': ['Animal Instincts','King of the Wild','Leaping Stag','Lord of the Hunt','Tooth and Claw','Tanglefoot'],
    'ulric': ['Crush the Weak','Frostbite','Heart of the Wolf','Hoarfrost Thews','Howl of Battle',"Hoarfrost's Chill",'Howl of the Wolf',"Ulric's Fury",'Pelt of The Winter Wolf',"The Snow King's Judgement","Winter's Bite","Wolf's Bite", 'Ice Storm'],
    'verena': ['As Verena is my Witness','Blind Justice','Shackles of Truth','Sword of Justice','Truth Will Out','Wisdom of the Owl']
}