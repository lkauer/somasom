from django import forms
from artist.models import Artist
from release.models import Release

class NewArtistForm(forms.ModelForm):
    ph_artist = forms.ImageField(label='Foto do artista', required=False)
    
    class Meta:
        model = Artist
        fields = ['nm_artist', 'ds_artist', 'ph_artist', 'user_id']

class NewReleaseForm(forms.ModelForm):
    ph_release = forms.ImageField(label='Foto do lançamento', required=False)
    
    class Meta:
        model = Release
        fields = ['nm_release', 'ds_release', 'ph_release']