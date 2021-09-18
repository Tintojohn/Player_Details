from django.shortcuts import render, redirect
from .forms import PlayersForm
from .models import *


# Create your views here.

def insertplayer(request):
    if request.method == 'GET':
        form = PlayersForm()
        return render(request, "players/insert_details.html", {'form': form})
    else:
        form = PlayersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('insert')

def player_list(request):
    list = Players.objects.all()
    return render(request, "players/players_details.html", {'p_list': list})
