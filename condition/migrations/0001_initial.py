# Generated by Django 3.1.6 on 2021-02-07 05:02

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
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, default=36.5, max_digits=3)),
                ('conditioning', models.BooleanField()),
                ('content', models.TextField(blank=True, max_length=1000)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('pub_time', models.TimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pub_date', '-pub_time'),
            },
        ),
    ]
