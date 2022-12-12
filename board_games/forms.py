from django import forms
from .models import Game, Gamers


class GameForm(forms.ModelForm):
    class Meta:
        model = 'Game'
        fields = ['name']
        labels = {'name':''}

class BorrowForm(forms.ModelForm):
  model=Player
  fields=['text']
  labels={'text':''}
  widgets={'text':forms.Textarea(attrs={'cols':80})}