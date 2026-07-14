# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import TuteurForm, EleveForm, InscriptionForm
from .models import Tuteur, Eleve, Inscription
from django.db.models import Count
from django.db.models.functions import ExtractMonth
import datetime, json

# Page d'accueil : Formulaire de connexion
def connexion_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Tableau de bord (uniquement accessible si connecté)
@login_required
def dashboard_view(request):
    # Comptages principaux
    stats = {
        'tuteurs_count': Tuteur.objects.count(),
        'eleves_count': Eleve.objects.count(),
        'inscriptions_count': Inscription.objects.count(),
    }

    # Dernière inscription
    last_inscription = Inscription.objects.select_related('matr_eleve', 'num_classe', 'num_option').order_by('-date_inscr', '-numinscription').first()

    # Statistiques mensuelles pour l'année en cours
    year = datetime.date.today().year
    monthly_qs = (
        Inscription.objects.filter(date_inscr__year=year)
        .annotate(month=ExtractMonth('date_inscr'))
        .values('month')
        .annotate(count=Count('pk'))
        .order_by('month')
    )

    # Préparer listes pour le chart (12 mois)
    month_labels = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
    month_data = [0] * 12
    for item in monthly_qs:
        m = int(item['month'])
        if 1 <= m <= 12:
            month_data[m-1] = item['count']

    # Sérialiser pour injection JS safe
    month_labels_json = json.dumps(month_labels)
    month_data_json = json.dumps(month_data)

    context = {
        'stats': stats,
        'last_inscription': last_inscription,
        'month_labels_json': month_labels_json,
        'month_data_json': month_data_json,
    }

    return render(request, 'dashboard.html', context)

# Ajouter un Tuteur
@login_required
def ajouter_tuteur(request):
    if request.method == 'POST':
        form = TuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TuteurForm()
    return render(request, 'ajouter_tuteur.html', {'form': form})

# Ajouter un Élève
@login_required
def ajouter_eleve(request):
    if request.method == 'POST':
        form = EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EleveForm()
    return render(request, 'ajouter_eleve.html', {'form': form})

# Ajouter une Inscription
@login_required
def ajouter_inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = InscriptionForm()
    return render(request, 'ajouter_inscription.html', {'form': form})

# Déconnexion
def deconnexion_view(request):
    logout(request)
    return redirect('login')