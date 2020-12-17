from django.db import models


# Create your models here.
class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(blank=False)
    RG = models.IntegerField()
    endereco = models.CharField(max_length=250)
    unidade_de_saude = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Vacina(models.Model):
    TIPOS = (
        ('DUPLA ADULTO', 'DUPLA ADULTO'),
        ('HEPATITE B', 'HEPATITE B'),
        ('SAR/CAX/RUB', 'SAR/CAX/RUB'),
        ('FEBRE AMARELA', 'FEBRE AMARELA')
    )
    ED = (
        ('PSF-CENTRO', 'PSF-CENTRO'),
        ('PSF-NORTE', 'PSF-NORTE'),
        ('PSF-SUL', 'PSF-SUL'),
        ('PSF-OESTE', 'PSF-OESTE')
    )
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,)
    vacina = models.CharField(max_length=15, choices=TIPOS, default='DUPLA ADULTO')
    local_disponivel = models.CharField(max_length=15, choices=ED, default='PSF-CENTRO')
    data = models.DateField(blank=False)
    lote = models.CharField(max_length=10)
    cod = models.IntegerField()
    nome = models.CharField(max_length=200)
    profissional = models.CharField(max_length=250)

    def __str__(self):
        template = '{0.paciente} - {0.vacina}'
        return template.format(self)
