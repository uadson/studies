from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=150)


class Editora(models.Model):
    nome = models.CharField(max_length=150)
    site = models.URLField()


class Autor(models.Model):
    nome = models.CharField(max_length=150)


class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    isbn = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='livros')
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name='livros')
    autores = models.ManyToManyField(Autor, related_name='livros')
