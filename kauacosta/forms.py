from django import forms 
from . import models

class alunoform(forms.ModelForm):
    class Meta:
        model = models.Aluno
        fields = '__all__'
