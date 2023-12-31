# Generated by Django 4.2.2 on 2023-06-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.BigIntegerField()),
                ('message', models.CharField(max_length=1000)),
                ('content', models.TextField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillname', models.CharField(max_length=50)),
                ('skillimage', models.ImageField(null=True, upload_to='skillimages')),
                ('skillquote', models.TextField(max_length=500)),
                ('skilldescription', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=100)),
                ('projectimage', models.ImageField(null=True, upload_to='projectimages')),
                ('teamsixze', models.IntegerField()),
                ('projectquote', models.TextField(max_length=1000)),
                ('projectroles', models.TextField(max_length=20000)),
                ('projectskills', models.ManyToManyField(to='myprofile.skills')),
            ],
        ),
    ]
