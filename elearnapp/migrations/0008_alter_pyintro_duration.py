# Generated by Django 4.1.1 on 2022-10-14 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearnapp', '0007_alter_pyintro_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyintro',
            name='duration',
            field=models.CharField(max_length=50),
        ),
    ]