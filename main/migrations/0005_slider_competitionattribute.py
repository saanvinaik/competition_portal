# Generated by Django 4.0.6 on 2022-09-02 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_competition'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('alt_text', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.competition')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.domain')),
                ('reg_fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reg_fees', to='main.competition')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.year')),
            ],
        ),
    ]
