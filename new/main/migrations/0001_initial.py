# Generated by Django 4.0.2 on 2022-02-08 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Type name')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Car name')),
                ('type_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.type')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
