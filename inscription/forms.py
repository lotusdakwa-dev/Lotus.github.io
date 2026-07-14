# forms.py
from django import forms
from .models import Tuteur, Eleve, Inscription

class TuteurForm(forms.ModelForm):
    class Meta:
        model = Tuteur
        fields = ['nom_tuteur', 'sexe_tuteur', 'tel_tuteur', 'adresse_tuteur']
        widgets = {
            'nom_tuteur': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe_tuteur': forms.Select(attrs={'class': 'form-control'}),
            'tel_tuteur': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse_tuteur': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['matr_eleve', 'nom_ele', 'pren_ele', 'tel_ele', 'adresse_ele', 'numtuteur']
        widgets = {
            'matr_eleve': forms.TextInput(attrs={'class': 'form-control'}),
            'nom_ele': forms.TextInput(attrs={'class': 'form-control'}),
            'pren_ele': forms.TextInput(attrs={'class': 'form-control'}),
            'tel_ele': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse_ele': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'numtuteur': forms.Select(attrs={'class': 'form-control'}),
        }

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['matr_eleve', 'num_option', 'num_classe']
        widgets = {
            'matr_eleve': forms.Select(attrs={'class': 'form-control'}),
            'num_option': forms.Select(attrs={'class': 'form-control'}),
            'num_classe': forms.Select(attrs={'class': 'form-control'}),
        }