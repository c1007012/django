# Generated by Django 4.2.6 on 2023-11-06 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Hardware', 'Hardware'), ('Software', 'Software')], max_length=100)),
                ('room', models.CharField(max_length=100)),
                ('urgent', models.BooleanField(default=False)),
                ('details', models.TextField()),
                ('date_submitted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
