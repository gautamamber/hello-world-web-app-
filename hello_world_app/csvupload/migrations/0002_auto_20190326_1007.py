# Generated by Django 2.1.7 on 2019-03-26 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csvupload', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CsvUpload',
            new_name='Person',
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'Person'},
        ),
    ]
