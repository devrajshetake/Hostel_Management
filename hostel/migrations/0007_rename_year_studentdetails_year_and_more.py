# Generated by Django 4.0.2 on 2022-05-08 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0006_remove_studentdetails_user_studentdetails_year_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdetails',
            old_name='YEAR',
            new_name='year',
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='aadhar',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='gnumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='roll',
            field=models.IntegerField(null=True),
        ),
    ]