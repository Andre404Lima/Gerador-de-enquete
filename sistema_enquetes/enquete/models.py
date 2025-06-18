from django.db import models
from django.utils import timezone

class Enquete(models.Model):
    pergunta = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_encerramento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.pergunta
    
    def encerrada(self):
        if self.data_encerramento:
            return timezone.now() >= self.data_encerramento
        return False
    
class Opcao(models.Model):
    enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE, related_name='opcoes')
    texto_opcao = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_opcao
