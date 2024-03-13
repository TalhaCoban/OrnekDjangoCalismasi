# Generated by Django 3.0.8 on 2020-08-15 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='YKS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytham', models.TextField(default=500, max_length=3, verbose_name='TYTham')),
                ('tytyer', models.TextField(default=500, max_length=3, verbose_name='TYTyer')),
                ('sayisalham', models.TextField(default=500, max_length=3, verbose_name='Sayisalham')),
                ('sayisalyer', models.TextField(default=500, max_length=3, verbose_name='Sayisalyer')),
                ('eaham', models.TextField(default=500, max_length=3, verbose_name='Eaham')),
                ('eayer', models.TextField(default=500, max_length=3, verbose_name='Eayer')),
                ('sozelham', models.TextField(default=500, max_length=3, verbose_name='Sozelham')),
                ('sozelyer', models.TextField(default=500, max_length=3, verbose_name='Sozelyer')),
                ('ydtham', models.TextField(default=500, max_length=3, verbose_name='Ydtham')),
                ('ydtyer', models.TextField(default=500, max_length=3, verbose_name='Ydtyer')),
                ('siralamalar', models.TextField(default='', max_length=200, verbose_name='Siralamalar')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('ogrenci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ogrenci')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]