# Generated by Django 5.0.6 on 2024-05-31 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_firstpage_bg_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='JourneyBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h2', models.CharField(max_length=50)),
                ('skils', models.TextField()),
                ('organization', models.ImageField(upload_to='')),
                ('orga_link', models.URLField()),
            ],
        ),
    ]
