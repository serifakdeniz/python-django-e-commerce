# Generated by Django 5.1.4 on 2024-12-08 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0006_alter_markalar_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategoriler',
            options={'verbose_name': 'kategori', 'verbose_name_plural': 'kategoriler'},
        ),
    ]
