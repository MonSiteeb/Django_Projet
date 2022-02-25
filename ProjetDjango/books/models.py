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


class Newsletter(models.Model):
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class MailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title
