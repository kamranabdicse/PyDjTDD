# Generated by Django 4.2.3 on 2023-07-05 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Listing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(default=None, null=True)),
                ("owner", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=200)),
                ("description", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(default=None, null=True)),
                ("number", models.IntegerField()),
                ("name", models.CharField(max_length=100)),
                ("price", models.FloatField(default=0.0)),
                ("is_available", models.BooleanField(default=True)),
                (
                    "listing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reservation_system.listing",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(default=None, null=True)),
                ("name", models.CharField(max_length=100)),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("choose", "Choose"),
                            ("payment_pending", "Payment Pending"),
                            ("purchased", "Purchased"),
                        ],
                        default="choose",
                        max_length=20,
                    ),
                ),
                ("choose_time", models.DateTimeField(null=True)),
                ("purchased_time", models.DateTimeField(null=True)),
                ("tax_price", models.FloatField(default=0.0)),
                ("discount_price", models.FloatField(default=0.0)),
                ("price", models.FloatField(default=0.0)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reservation_system.room",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
