# Generated by Django 3.2 on 2021-12-14 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='candidate',
            unique_together={('cpf', 'email')},
        ),
    ]
