from django.shortcuts import render, redirect
from .models import Filmes, Opinioes


def home(request):
  filmes = Filmes.objects.all()
  opinioes = Opinioes.objects.all()
  return render(request, "home.html",context={"filmes": filmes, "opinioes": opinioes})

def create_movie(request):
  if request.method == "POST":
    Filmes.objects.create(
      titulo = request.POST["titulo"],
      diretor = request.POST["diretor"],
      genero = request.POST["genero"],
      anoLancamento = request.POST["anoLancamento"]
    )
    
    return redirect("home")
  return render(request, "forms.html", context={"action":"Adicionar"})

def update_movie(request, id):
  movie = Filmes.objects.get(id = id)
  if request.method == "POST":
    movie.titulo = request.POST["titulo"]
    movie.diretor = request.POST["diretor"]
    movie.genero = request.POST["genero"]
    movie.anoLancamento = request.POST["anoLancamento"]
    movie.save()
    
    return redirect("home")
  return render(request, "forms.html", context={"action":"Atualizar","movie": movie})

def delete_movie(request, id):
  movie = Filmes.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      movie.delete()
    return redirect("home")
  return render(request, "are_you_sure.html", context={"movie": movie})

def create_opinion(request):
  if request.method == "POST":
    Opinioes.object.create(
      headlineDaOpiniao = request.POST["headlineDaOpiniao"],
      tituloFilme = request.POST["tituloFilme"],
      diretorFilme = request.POST["diretorFilme"],
      anoLancamentoFilme = request.POST["anoLancamentoFilme"]
    )
    
    return redirect("home")
  return render(request, "forms.html", context={"action":"Adicionar"})

def update_opinion(request, id):
  opinion = Opinioes.objects.get(id = id)
  if request.method == "POST":
    opinion.headlineDaOpiniao = request.POST["headlineDaOpiniao"]
    opinion.tituloFilme = request.POST["tituloFilme"]
    opinion.diretorFilme = request.POST["diretorFilme"]
    opinion.anoLancamentoFilme = request.POST["anoLancamentoFilme"]
    opinion.save()
    
    return redirect("home")
  return render(request, "forms.html", context={"action":"Atualizar","opinion": opinion})

def delete_opinion(request, id):
  opinion = Opinioes.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      opinion.delete()
    return redirect("home")
  return render(request, "are_you_sure.html", context={"opinion": opinion})