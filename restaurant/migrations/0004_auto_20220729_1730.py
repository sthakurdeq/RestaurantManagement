# Generated by Django 3.2 on 2022-07-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0003_auto_20220729_1233"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menu",
            name="vote",
        ),
        migrations.RemoveField(
            model_name="ratings",
            name="timestamp",
        ),
        migrations.AddField(
            model_name="ratings",
            name="vote",
            field=models.CharField(
                choices=[(-1, "Dislike"), (0, "Neutral"), (1, "Like")],
                default="Dislike",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="item",
            field=models.ManyToManyField(to="restaurant.Item"),
        ),
    ]
