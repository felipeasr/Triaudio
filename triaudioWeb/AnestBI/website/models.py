from django.db import models
from django.contrib import admin

# Register your models here.

# Create your models here.
class usuario (models.Model):
    """Model representing an usuario."""
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    class Meta:
        ordering = ['cpf', 'nome']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('usuario-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.cpf}, {self.nome}'

class teste (models.Model):
    """Model representing an usuario."""
    data_teste = models.CharField(max_length=100)
    tipo_teste = models.CharField(max_length=100)
    orelha_direita_teste =models.CharField(max_length=100)
    orelha_esquerda_teste = models.CharField(max_length=100)
    conduta_teste = models.CharField(max_length=100)
    observacoes = models.CharField(max_length=100)


    class Meta:
        ordering = ['data_teste']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('teste-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.data_teste}'
