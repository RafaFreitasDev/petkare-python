from django.db import models

class PetSex(models.TextChoices):
    male = "Male"
    female = "Female"
    not_info = "Not Informed"

class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=20, choices=PetSex.choices, default=PetSex.not_info)

    group = models.ForeignKey(
        "groups.Group", on_delete=models.PROTECT, related_name="pets"
    )

    traits = models.ManyToManyField(
        "traits.Trait", related_name="traits"
    )