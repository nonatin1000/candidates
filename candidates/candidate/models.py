from django.db import models
from django.utils.translation import ugettext_lazy as _


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name=_("Nome"), max_length=100)
    email = models.EmailField(verbose_name=_("_E-mail"), unique=True)
    cpf = models.CharField(verbose_name=_("_CPF"), max_length=11, unique=True)
    age = models.IntegerField(verbose_name=_("_Idade"))
    salary_claim = models.DecimalField(
        verbose_name=_("_Prentenção Salarial"),
        decimal_places=2,
        max_digits=9
    )
    is_immediate_availability_for_work = models.BooleanField(
        verbose_name=_("_Disponibilidade imediata para trabalho"),
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('cpf', 'email')
