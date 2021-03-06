# Generated by Django 3.2.4 on 2021-06-18 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
        ('book', '0005_alter_bookrevision_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcontent',
            name='modifiedBy',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='authorization.user'),
        ),
        migrations.AlterField(
            model_name='bookrevision',
            name='content',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_revision_content', to='book.bookcontent'),
        ),
    ]
