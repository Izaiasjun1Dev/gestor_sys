from django.db import models

class Departamentos(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do departamento')

    def __str__(self):
        return self.nome