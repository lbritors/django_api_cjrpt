from django.db import models

# Create your models here.


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=140)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    fotoPerfil = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    disciplinas = models.ManyToManyField('Disciplina', related_name='professores')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Disciplina(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Avaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    conteudo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='avaliacoes')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='avaliacoes')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='avaliacoes')


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    conteudo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='comentarios')