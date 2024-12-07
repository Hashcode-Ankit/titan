# Generated by Django 2.2.1 on 2019-05-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stories", "0005_auto_20190525_2320"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="epicstate",
            options={"ordering": ["stype", "name"]},
        ),
        migrations.AlterModelOptions(
            name="storystate",
            options={"ordering": ["stype", "name"]},
        ),
        migrations.AlterField(
            model_name="epicstate",
            name="stype",
            field=models.PositiveIntegerField(
                choices=[(0, "Unstarted"), (1, "Started"), (2, "Done")], db_index=True, default=0
            ),
        ),
        migrations.AlterField(
            model_name="storystate",
            name="stype",
            field=models.PositiveIntegerField(
                choices=[(0, "Unstarted"), (1, "Started"), (2, "Done")], db_index=True, default=0
            ),
        ),
    ]