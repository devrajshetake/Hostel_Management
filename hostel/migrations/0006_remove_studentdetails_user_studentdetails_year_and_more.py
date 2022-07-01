# Generated by Django 4.0.2 on 2022-05-08 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_studentdetails_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetails',
            name='user',
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='YEAR',
            field=models.CharField(choices=[('FE', 'FE'), ('SE', 'SE'), ('TE', 'TE'), ('BE', 'BE')], default='FE', max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='branch',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='reg',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='roll',
            field=models.IntegerField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='mob1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='mob2',
            field=models.IntegerField(null=True),
        ),
    ]
