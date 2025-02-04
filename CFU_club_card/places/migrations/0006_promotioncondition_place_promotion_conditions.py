# Generated by Django 5.1.5 on 2025-02-02 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_category_place_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='promotion_conditions',
            field=models.ManyToManyField(blank=True, related_name='places', to='places.promotioncondition'),
        ),
    ]
