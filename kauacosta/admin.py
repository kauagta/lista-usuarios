from django.contrib import admin

from . import models
@admin.register(models.Aluno)

class AlunoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'idade', 'numero', 'email', ]
