# Generated by Django 3.2.4 on 2021-06-18 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20210618_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcontent',
            name='revision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_content_revision', to='book.bookrevision'),
        ),
    ]
