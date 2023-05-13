from django import forms
from NPCGenerator4e.info.career_info import career_list
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

species_list = [
    ('random', 'Random'),
    ('dwarf','Dwarf'),
    ('halfling','Halfling'),
    ('human','Human'),
    ('high elf','High Elf'),
    ('wood elf', 'Wood Elf')
    ]

gender_list = [
    ('random', 'Random'),
    ('female','Female'),
    ('male','Male')
    ]

career_path = [
    ('random', 'Random'),
    ('academic','Academic'),
    ('burgher','Burgher'),
    ('courtier','Courtier'),
    ('peasant','Peasant'),
    ('ranger','Ranger'),
    ('riverfolk','Riverfolk'),
    ('rogue','Rogue'),
    ('warrior','Warrior')

    ]

xp_list = [
    ('random', 'Random'),
    (1, '1 (Starting Character)'),
    (1.5, '1 (Advanced)'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    ]
###

career_list =[('random','Random'),('advisor','Advisor'),('agitator','Agitator'),('apothecary','Apothecary'),('artisan','Artisan'),('artist','Artist'),('bailiff','Bailiff'),('bawd','Bawd'),
('beggar','Beggar'),('boatman','Boatman'),('bounty hunter','Bounty hunter'),('cavalryman','Cavalryman'),('charlatan','Charlatan'),('coachman','Coachman'),('duellist','Duellist'),('engineer','Engineer'),
('entertainer','Entertainer'),('envoy','Envoy'),('fence','Fence'),('flagellant','Flagellant'),('grave robber','Grave Robber'),('guard','Guard'),('hedge witch','Hedge Witch'),('herbalist','Herbalist'),
('huffer','Huffer'),('hunter','Hunter'),('investigator','Investigator'),('knight','Knight'),('lawyer','Lawyer'),('merchant','Merchant'),('messenger','Messenger'),('miner','Miner'),('mystic','Mystic'),
('noble','Noble'),('nun','Nun'),('outlaw','Outlaw'),('pedlar','Pedlar'),('physician','Physician'),('pit fighter','Pit Fighter'),('priest','Priest'),('protagonist','Protagonist'),('racketeer','Racketeer'),
('rat catcher','Rat Catcher'),('riverwarden','Riverwarden'),('riverwoman','Riverwoman'),('road warden','Road Warden'),('scholar','Scholar'),('scout','Scout'),('seaman','Seaman'),('servant','Servant'),
('slayer','Slayer'),('smuggler','Smuggler'),('soldier','Soldier'),('spy','Spy'),('stevedore','Stevedore'),('thief','Thief'),('townsman','Townsman'),('villager','Villager'),('warden','Warden'),
('warrior priest','Warrior Priest'),('watchman','Watchman'),('witch hunter','Witch Hunter'),('witch','Witch'),('wizard','Wizard'),('wrecker','Wrecker'),]


book_list = [
    ('windsOfMagic', 'Winds of Magic'),('upInArms','Up in Arms')
]

class NPCGenerator(forms.Form):
    species = forms.CharField(label='Character Species:',initial='random', widget=forms.RadioSelect(choices=species_list))
    gender= forms.CharField(label='Character Gender:',initial='random', widget=forms.RadioSelect(choices=gender_list))
    experience= forms.CharField(label='Level:', widget=forms.Select(choices=xp_list))
    path= forms.CharField(label='Career Path:', widget=forms.Select(choices=career_path))
    career= forms.CharField(label='Specific Career:', widget=forms.Select(choices=career_list))
    books = forms.MultipleChoiceField(
    required=False,
    widget=forms.CheckboxSelectMultiple,
    choices=book_list
    )


