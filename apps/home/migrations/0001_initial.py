# Generated by Django 3.2.6 on 2022-01-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaksinasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('vac_able', models.IntegerField()),
                ('vac_done', models.IntegerField()),
            ],
        ),
    ]