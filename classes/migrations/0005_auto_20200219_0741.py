# Generated by Django 2.1.5 on 2020-02-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20200219_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='exam_grade',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]