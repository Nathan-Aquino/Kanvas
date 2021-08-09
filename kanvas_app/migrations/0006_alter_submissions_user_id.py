# Generated by Django 3.2.6 on 2021-08-08 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kanvas_app', '0005_alter_submissions_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
