# Generated by Django 2.1.7 on 2019-03-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadcsvadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_class',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]