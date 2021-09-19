from django.shortcuts import render, redirect
from .forms import PlayersForm
from .models import *
from django.db.models import Count, Sum, F


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

def edit(request,id):
    if request.method == 'GET':
        pl = Players.objects.get(pk=id)
        form = PlayersForm(instance=pl)
        return render(request, "players/update.html", {'form': form})
    else:
        pl = Players.objects.get(pk=id)
        form = PlayersForm(request.POST, instance=pl)
        if form.is_valid():
            form.save()
        return redirect('/list')

def pl_delete(request, id):
    pl = Players.objects.get(pk=id)
    pl.delete()
    return redirect('/list')

def top_players(request):
    list =(Players.objects.values('Players_Id', 'Player_Name', 'Player_Email', 'Country').alias(games=Count('Game'), total=Sum('Score')).annotate(games=F('games'), total=F('total')).order_by('-total'))
    return render(request, "players/top_players.html", {'top_list': list})
