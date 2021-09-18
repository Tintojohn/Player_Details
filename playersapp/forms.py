from .models import Players
from django import forms
class PlayersForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = ('Players_Id', 'Player_Name', 'Player_Email', 'Country', 'Game', 'Score')
        labels = {
            'Players_Id': 'ID',
            'Player_Name': 'Player Name',
            'Player_Email': 'Player Email',
            'Country': 'Country',
            'Game': 'Game',
            'Score': 'Score'
        }