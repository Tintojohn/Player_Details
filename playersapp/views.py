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

def edit(request,Players_Id):
    if request.method == 'GET':
        pl = Players.objects.get(pk=Players_Id)
        form = PlayersForm(instance=pl)
        return render(request, "players/update.html", {'form': form})
    else:
        pl = Players.objects.get(pk=Players_Id)
        form = PlayersForm(request.POST, instance=pl)
        if form.is_valid():
            form.save()
        return redirect('/list')

def pl_delete(request, Players_Id):
    pl = Players.objects.get(pk=Players_Id)
    pl.delete()
    return redirect('/list')
