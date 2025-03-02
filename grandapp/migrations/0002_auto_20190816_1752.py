# Generated by Django 2.1 on 2019-08-16 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grandapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellLine', models.CharField(max_length=100)),
                ('cellLink', models.URLField()),
                ('tool', models.CharField(max_length=100)),
                ('netzoo', models.FloatField()),
                ('network', models.URLField()),
                ('ppi', models.URLField()),
                ('ppiLink', models.URLField()),
                ('motif', models.URLField()),
                ('expression', models.URLField()),
                ('expLink', models.URLField()),
                ('tfs', models.IntegerField()),
                ('genes', models.IntegerField()),
                ('refs', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='pet',
            name='vaccinations',
        ),
        migrations.DeleteModel(
            name='Pet',
        ),
    ]
