from ast import Del
from django.shortcuts import render, redirect

from . import models, forms
def base(request):
    aluno = models.Aluno.objects.all()
    return render(request, 'base.html', {'aluno':aluno})
def base2(request):
        aluno = models.Aluno.objects.all()
    # form = forms.alunoform(request.POST or None)

    # if form.is_valid():
    #     form.save()
    #     return redirect('base')
    # else:
        return render(request, 'base2.html', {'aluno':aluno})
    
def delete(request, id):
    delete = models.aluno.objects.get(id=id)
    delete.delete()
    return redirect('base')


    return render(request, 'base2.html')