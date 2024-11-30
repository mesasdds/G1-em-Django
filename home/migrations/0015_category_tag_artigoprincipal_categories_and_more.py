# Generated by Django 5.0.2 on 2024-07-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_artigosrecommends'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='artigoprincipal',
            name='categories',
            field=models.ManyToManyField(blank=True, to='home.category'),
        ),
        migrations.AddField(
            model_name='artigosecundario',
            name='categories',
            field=models.ManyToManyField(blank=True, to='home.category'),
        ),
        migrations.AddField(
            model_name='artigosgenericos',
            name='categories',
            field=models.ManyToManyField(blank=True, to='home.category'),
        ),
        migrations.AddField(
            model_name='artigosrecommends',
            name='categories',
            field=models.ManyToManyField(blank=True, to='home.category'),
        ),
        migrations.AddField(
            model_name='artigoterceiro',
            name='categories',
            field=models.ManyToManyField(blank=True, to='home.category'),
        ),
        migrations.AddField(
            model_name='artigoprincipal',
            name='tags',
            field=models.ManyToManyField(blank=True, to='home.tag'),
        ),
        migrations.AddField(
            model_name='artigosecundario',
            name='tags',
            field=models.ManyToManyField(blank=True, to='home.tag'),
        ),
        migrations.AddField(
            model_name='artigosgenericos',
            name='tags',
            field=models.ManyToManyField(blank=True, to='home.tag'),
        ),
        migrations.AddField(
            model_name='artigosrecommends',
            name='tags',
            field=models.ManyToManyField(blank=True, to='home.tag'),
        ),
        migrations.AddField(
            model_name='artigoterceiro',
            name='tags',
            field=models.ManyToManyField(blank=True, to='home.tag'),
        ),
    ]