from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def cursos(request):
    return render(request, 'cursos.html')

def contato(request):
    return render(request, 'contato.html')

def login(request):
    return render(request, 'login.html')

def disciplinaADS(request):
    return render(request, 'disciplinaADS.html')

def novaDisciplina(request):
    return render(request, 'novaDisciplina.html')

def novoAluno(request):
    return render(request, 'novoAluno.html')

def novoCurso(request):
    return render(request, 'novoCurso.html')
    
def detalhesDisciplina(request):
    return render(request, 'detalhesDisciplina.html')

def matricula(request):
    return render(request, 'matricula.html')