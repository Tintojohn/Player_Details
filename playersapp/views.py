from django.shortcuts import render, redirect
from .forms import PlayersForm


# Create your views here.

def insert_player(request):
    if request.method == 'GET':
        form = PlayersForm()
        return render(request, "players/insert_details.html", {'form': form})
    else:
        form = PlayersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('insert')
