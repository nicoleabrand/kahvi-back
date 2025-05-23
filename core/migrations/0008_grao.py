# Generated by Django 5.1.7 on 2025-05-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_produto_estoque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('estoque', models.IntegerField(default=0)),
                ('imagem', models.ImageField(upload_to='produtos/')),
                ('intensidade', models.CharField(max_length=255)),
                ('sabor', models.CharField(max_length=255)),
                ('aroma', models.CharField(max_length=255)),
                ('torra', models.CharField(max_length=255)),
                ('acidez', models.CharField(max_length=255)),
                ('corpo', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('variedade', models.CharField(max_length=255)),
                ('processo', models.CharField(max_length=255)),
                ('origem', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
            ],
        ),
    ]
