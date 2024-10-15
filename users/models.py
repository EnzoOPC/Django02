from django.db import models


class User(models.Model):

    name = models.CharField(verbose_name="nome", max_length=50, null=False, blank=False)

    birthDate = models.DateField(verbose_name="Nascido em", null=False, blank=False)

    cpf = models.IntegerField(verbose_name="CPF", null=False, blank=False)

    email = models.EmailField(
        verbose_name="E-mail", max_length=255, null=False, blank=False
    )

    created_at = models.DateTimeField(
        verbose_name="Criado em", auto_now_add=True, null=False, blank=False
    )
