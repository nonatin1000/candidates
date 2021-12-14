# Generated by Django 3.2 on 2021-12-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='_E-mail')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='_CPF')),
                ('age', models.IntegerField(verbose_name='_Idade')),
                ('salary_claim', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='_Prentenção Salarial')),
                ('is_immediate_availability_for_work', models.BooleanField(default=False, verbose_name='_Disponibilidade imediata para trabalho')),
            ],
        ),
    ]