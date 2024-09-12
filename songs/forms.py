from django.forms import ModelForm, Form
from django import forms
from .models import Song

class SongUpload(ModelForm):
    name = forms.TextInput()
    singer = forms.TextInput()
    song_image= forms.FileInput()
    song_file = forms.FileInput()

    class Meta:
        model=Song
        fields = ["name", "singer", "song_image", "song_file"]

