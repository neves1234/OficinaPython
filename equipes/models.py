from django.db import models

class Equipe(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Mecanico(models.Model):
    mecanico = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=18)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.mecanico
