# Generated by Django 2.0.7 on 2018-08-25 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0014_auto_20180824_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimgs',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Project'),
        ),
    ]