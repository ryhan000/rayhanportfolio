# Generated by Django 2.1.7 on 2019-03-19 05:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('objective', models.TextField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('profile_images', models.ImageField(blank=True, null=True, upload_to='images/reviews/')),
                ('phone', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+8801XXXXXXXXX'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.CharField(max_length=100)),
                ('birth_day', models.DateField()),
                ('marital_status', models.CharField(blank=True, choices=[('married', 'Married'), ('unmarried', 'Unmarried')], max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('personal_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutme.PersonalInfo')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='images/reviews/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutme.Project')),
            ],
        ),
    ]