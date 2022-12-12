from django import forms
from .models import Game, Borrow



class GameForm(forms.ModelForm):
    class Meta:
        model = 'Game'
        fields = ['name']
        labels = {'name':''}

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}