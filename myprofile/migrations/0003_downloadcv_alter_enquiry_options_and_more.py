# Generated by Django 4.2 on 2023-06-24 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_alter_skills_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='downloadcv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='files')),
            ],
        ),
        migrations.AlterModelOptions(
            name='enquiry',
            options={'verbose_name_plural': 'Enquiries'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Projects'},
        ),
    ]
