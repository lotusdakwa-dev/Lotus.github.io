from django.db import models

class Classe(models.Model):
    numclasse = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle


class Option(models.Model):
    numoption = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.libelle


class Tuteur(models.Model):
    CHOIX_SEXE = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    numtuteur = models.AutoField(primary_key=True)
    nom_tuteur = models.CharField(max_length=100)
    sexe_tuteur = models.CharField(max_length=1, choices=CHOIX_SEXE)
    tel_tuteur = models.CharField(max_length=20)
    adresse_tuteur = models.TextField()

    def __str__(self):
        return self.nom_tuteur


class Eleve(models.Model):
    matr_eleve = models.CharField(max_length=50, primary_key=True) # Modifier en AutoField si c'est un ID automatique
    nom_ele = models.CharField(max_length=100)
    pren_ele = models.CharField(max_length=100)
    tel_ele = models.CharField(max_length=20, blank=True, null=True)
    adresse_ele = models.TextField()
    
    # Clé étrangère vers Tuteur
    numtuteur = models.ForeignKey(Tuteur, on_delete=models.CASCADE, related_name='eleves')

    def __str__(self):
        return f"{self.nom_ele} {self.pren_ele}"


class Inscription(models.Model):
    numinscription = models.AutoField(primary_key=True)
    date_inscr = models.DateField(auto_now_add=True) # Enregistre automatiquement la date du jour
    
    # Clés étrangères
    matr_eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE, related_name='inscriptions')
    num_option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='inscriptions')
    num_classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name='inscriptions')

    def __str__(self):
        return f"Inscription N° {self.numinscription} - {self.matr_eleve}"
