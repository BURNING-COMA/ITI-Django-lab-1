# Generated by Django 4.0.2 on 2022-02-06 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amazon', '0003_alter_intake_end_date_alter_intake_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='intake_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='amazon.intake'),
        ),
        migrations.AlterField(
            model_name='student',
            name='track_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='amazon.track'),
        ),
    ]
