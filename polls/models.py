from django.db import models
from django.utils import timezone

class Hospede(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Gerente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


class Quarto(models.Model):
    id = models.AutoField(primary_key=True)
    numero_quarto = models.CharField(max_length=10, unique=True)
    tipo_quarto = models.CharField(max_length=50)
    preco_por_noite = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('disponível', 'Disponível'),
        ('ocupado', 'Ocupado'),
        ('em manutenção', 'Em Manutenção'),
    ], default='disponível')

    def __str__(self):
        return f"Quarto {self.numero_quarto} - {self.tipo_quarto}"


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    hospede = models.ForeignKey(Hospede, on_delete=models.CASCADE, related_name='reservas')
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, related_name='reservas')
    data_check_in = models.DateTimeField()
    data_check_out = models.DateTimeField()
    status_reserva = models.CharField(max_length=20, choices=[
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ], default='confirmada')
    data_reserva = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reserva {self.id} - {self.hospede} - {self.quarto}"
