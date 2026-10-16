from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
    
class Tecnico(models.Model):
    nome = models.CharField(max_length=65)
    email = models.EmailField(validators=True)
    telefone = models.CharField(max_length=25)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Tecnico'
        verbose_name = 'Tecnicos'
    
    def __str__(self):
        return self.nome
    
class Equipe(models.Model):
    nome = models.CharField(max_length=65, unique= True)
    curso = models.CharField(max_length=65)
    cor = models.CharField(max_length=25)
    criada_em = models.DateTimeField(auto_now_add=True)
    tecnico = models.OneToOneField(Tecnico, unique=True, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['curso']
        verbose_name = 'Equipe'
        verbose_name = 'Equipes'
                
    def __str__(self):
        return self.nome
  
class Modalidade(models.Model):
    nome = models.CharField(max_length=250, unique=True)
    tipo = models.Choices("Coletivo", "Individual")
    max_atletas = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Modalidade'
        verbose_name = 'Modalidades'
    
    def __str__(self):
        return self.nome
    
class Atleta(models.Model):
    nome = models.CharField(max_length=65)
    matricula = models.CharField(max_length=65, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey(Equipe, blank=True, on_delete=models.PROTECT)
    modalidades = models.ManyToManyField(Modalidade, blank=True)
    
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Atleta'
        verbose_name = 'Atletas'
        
    def __str__(self):
        return self.matricula
    


        

