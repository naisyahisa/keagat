# Generated by Django 3.2.6 on 2022-02-09 15:36

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpeg', upload_to='profile_pics')),
                ('bg_image', models.ImageField(default='bgdefault.jpeg', upload_to='bg_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Helpdesk',
            fields=[
                ('help_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('help_status', models.CharField(max_length=30)),
                ('help_subject', models.CharField(max_length=50)),
                ('help_content', models.CharField(max_length=500)),
                ('date_created', models.DateField(auto_now=True)),
                ('help_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
