# Generated by Django 3.2.4 on 2021-07-04 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjetoFinalPW', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clareza', models.IntegerField(choices=[(1, 'O site está horrível'), (2, 'O site está mau '), (3, 'O site está aceitável'), (4, 'O site está bom'), (5, 'O site está excelente')], default=3)),
                ('rigor', models.IntegerField(choices=[(1, 'O site está horrível'), (2, 'O site está mau '), (3, 'O site está aceitável'), (4, 'O site está bom'), (5, 'O site está excelente')], default=3)),
                ('profundidade', models.IntegerField(choices=[(1, 'O site está horrível'), (2, 'O site está mau '), (3, 'O site está aceitável'), (4, 'O site está bom'), (5, 'O site está excelente')], default=3)),
                ('layout', models.IntegerField(choices=[(1, 'O site está horrível'), (2, 'O site está mau '), (3, 'O site está aceitável'), (4, 'O site está bom'), (5, 'O site está excelente')], default=3)),
                ('logica', models.IntegerField(choices=[(1, 'O site está horrível'), (2, 'O site está mau '), (3, 'O site está aceitável'), (4, 'O site está bom'), (5, 'O site está excelente')], default=3)),
                ('estrutura', models.IntegerField(choices=[(1, 'O site está horrível'), (2, 'O site está mau '), (3, 'O site está aceitável'), (4, 'O site está bom'), (5, 'O site está excelente')], default=3)),
                ('originalidade', models.IntegerField(choices=[(1, 'O site está horrível'), (2, 'O site está mau '), (3, 'O site está aceitável'), (4, 'O site está bom'), (5, 'O site está excelente')], default=3)),
                ('cores', models.IntegerField(choices=[(1, 'O site está horrível'), (2, 'O site está mau '), (3, 'O site está aceitável'), (4, 'O site está bom'), (5, 'O site está excelente')], default=3)),
                ('animacoes', models.IntegerField(choices=[(1, 'O site está horrível'), (2, 'O site está mau '), (3, 'O site está aceitável'), (4, 'O site está bom'), (5, 'O site está excelente')], default=3)),
            ],
        ),
    ]
