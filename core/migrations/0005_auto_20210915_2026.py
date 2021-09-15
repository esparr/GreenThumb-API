# Generated by Django 3.2.7 on 2021-09-15 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_answer_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.question'),
        ),
    ]
