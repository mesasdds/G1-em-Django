# Generated by Django 4.2 on 2023-05-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_artigoprincipal_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigoprincipal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='artigosecundario',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='artigoterceiro',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]