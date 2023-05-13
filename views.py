from cmd import IDENTCHARS
from django.shortcuts import render, redirect
import random
from .NPCGenerator import GenerateNPC
from .forms import NPCGenerator
from django.contrib import messages
from django.utils.html import escape
# Create your views here.
def home(request):

    return render(request, 'NPCGenerator/NPCCreator.html')

def createNPC(request):    
    form = NPCGenerator(request.POST)
    if len(request.POST) != 0:
        npc = GenerateNPC(request.POST["species"],request.POST["path"], request.POST["gender"],request.POST["career"], request.POST["experience"], request.POST.getlist('books'))       
        context ={"npc": npc, "form": form}
        npc.npc['char']['total_stats'] = []
        for x in range(0, len(npc.npc['char']['attributeAdvances'])):#
            npc.npc['char']['total_stats'].append(int((npc.npc['char']['attributes'][x]) + int(npc.npc['char']['attributeAdvances'][x]))) #

        npc.npc['char']['speciesTalents'].sort()	
        npc.npc['char']['careerTalents'].sort()	        
        return render(request, 'NPCGenerator4e/NPCCreator.html', context)
    else:
        context=""
    return render(request, 'NPCGenerator4e/NPCCreator.html', {"form":form})




