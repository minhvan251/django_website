# Generated by Django 3.0.4 on 2020-03-27 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title', '-publication_date']},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='tittle',
            new_name='title',
        ),
    ]