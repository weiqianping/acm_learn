# Generated by Django 5.1.1 on 2024-10-13 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0002_studentsprofile_class_name_studentsprofile_college_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/'),
        ),
    ]
