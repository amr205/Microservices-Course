# Generated by Django 4.1.5 on 2023-01-25 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genres',
            field=models.ManyToManyField(to='recommendations_app.genre'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=512, primary_key=True, serialize=False)),
                ('genres', models.ManyToManyField(to='recommendations_app.genre')),
            ],
        ),
    ]
