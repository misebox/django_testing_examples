# Generated by Django 3.2.6 on 2021-08-26 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Combo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('combo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.combo')),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ref_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('repo_url', models.URLField(max_length=300)),
                ('since_date', models.DateField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('combo_set', models.ManyToManyField(related_name='package_set', through='packages.Composition', to='packages.Combo')),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='packages', to='packages.programminglanguage')),
            ],
        ),
        migrations.AddField(
            model_name='composition',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='packages.package'),
        ),
    ]