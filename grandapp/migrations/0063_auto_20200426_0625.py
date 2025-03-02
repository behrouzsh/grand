# Generated by Django 3.0.5 on 2020-04-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grandapp', '0062_auto_20200426_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='gwas',
            name='idd',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tissueex',
            name='idd',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tissuetar',
            name='idd',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gwas',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tissueex',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tissuetar',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
