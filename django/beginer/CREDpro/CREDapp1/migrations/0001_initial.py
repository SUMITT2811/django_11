# Generated by Django 5.1.4 on 2024-12-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('sId', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=100)),
                ('sprice', models.FloatField(default=0.0)),
                ('size', models.IntegerField()),
                ('sBrand', models.CharField(max_length=100)),
                ('stype', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('MEN', 'men'), ('WOMEN', 'women'), ('KIDS', 'kids')], default='active', max_length=10)),
            ],
        ),
    ]
