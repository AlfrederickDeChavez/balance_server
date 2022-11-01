from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    quantity = models.FloatField()
    date_consumed = models.DateTimeField()
    user = models.ManyToManyField(User)
    calories = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    dietary_fiber = models.FloatField(null=True, blank=True)
    vitamin_A = models.FloatField(null=True, blank=True)
    vitamin_D = models.FloatField(null=True, blank=True)
    vitamin_E = models.FloatField(null=True, blank=True)
    vitamin_K = models.FloatField(null=True, blank=True)
    thiamin = models.FloatField(null=True, blank=True)
    riboflavin = models.FloatField(null=True, blank=True)
    niacin = models.FloatField(null=True, blank=True)
    vitamin_B6 = models.FloatField(null=True, blank=True)
    vitamin_B12 = models.FloatField(null=True, blank=True)
    folate = models.FloatField(null=True, blank=True)
    vitamin_C = models.FloatField(null=True, blank=True)
    iron = models.FloatField(null=True, blank=True)
    zinc = models.FloatField(null=True, blank=True)
    selenium = models.FloatField(null=True, blank=True)
    iodine = models.FloatField(null=True, blank=True)
    calcium = models.FloatField(null=True, blank=True)
    magnesium = models.FloatField(null=True, blank=True)
    phosphorus = models.FloatField(null=True, blank=True)
    flouride = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    chloride = models.FloatField(null=True, blank=True)
    potassium = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name