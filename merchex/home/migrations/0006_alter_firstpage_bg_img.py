# Generated by Django 5.0.6 on 2024-05-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_firstpage_bg_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstpage',
            name='bg_img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
