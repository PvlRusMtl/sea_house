# Generated by Django 3.2.16 on 2022-11-14 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0003_auto_20221113_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('phone', models.CharField(max_length=50, verbose_name='phone')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.house', verbose_name='house')),
            ],
        ),
    ]
