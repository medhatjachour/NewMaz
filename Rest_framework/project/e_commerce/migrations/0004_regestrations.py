# Generated by Django 4.0.3 on 2022-03-22 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0003_user_account_user_account_hash_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regestrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('email', models.CharField(max_length=75)),
                ('password', models.CharField(max_length=75)),
            ],
        ),
    ]