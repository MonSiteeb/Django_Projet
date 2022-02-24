from django.db import models

class Documents(models.Model):
    catchoice= [
        ('epreuve', 'Epreuve'),
        ('correction', 'Correction'),
        ]
    matiere=models.CharField(max_length=30)
    classe=models.CharField(max_length=30)
    professeur=models.CharField(max_length=40)
    categorie=models.CharField(max_length=30,choices=catchoice,default='epreuve')
    fichier=models.FileField()
    def __str__(self):
        return str(self.name)+"["+str(self.classe)+']'