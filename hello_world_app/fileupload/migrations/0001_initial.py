# Generated by Django 2.1.7 on 2019-03-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('text', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'File Upload',
                'verbose_name_plural': 'File Upload',
            },
        ),
    ]