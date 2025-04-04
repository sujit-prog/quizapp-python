# Generated by Django 5.1.7 on 2025-04-03 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_question_text_question_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer_text',
            new_name='answer',
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='home.category'),
        ),
    ]
