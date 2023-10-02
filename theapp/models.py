from django.db import models

# Create your models here.
class Filmes(models.Model):
  titulo = models.CharField(max_length=70)
  diretor = models.CharField(max_length=70)
  genero = models.CharField(max_length=20)
  anoLancamento = models.DateField()
  #nota = models.DecimalField(..., max_digits=3, decimal_places=1) - não funcionou, também tentei usar floatfield

class Opinioes(models.Model):
  headlineDaOpiniao = models.CharField(max_length=100)
  tituloFilme = models.CharField(max_length=70)
  diretorFilme = models.CharField(max_length=70)
  anoLancamentoFilme = models.DateField()
  #notaFilme = models.DecimalField(..., max_digits=3, decimal_places=1) - não funcionou, também tentei usar floatfield
  
  