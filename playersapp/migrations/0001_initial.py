# Generated by Django 3.2.4 on 2021-09-18 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Players_Id', models.IntegerField()),
                ('Player_Name', models.CharField(max_length=100)),
                ('Player_Email', models.EmailField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('Game', models.CharField(max_length=100)),
                ('Score', models.IntegerField()),
            ],
        ),
    ]
