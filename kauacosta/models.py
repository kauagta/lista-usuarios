from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    email = models.CharField(max_length=100)