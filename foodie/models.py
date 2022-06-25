from django.db import models

# Create your models here.
class FoodPlaza(models.Model):
    Dish_def = models.CharField(max_length=30)
    Item_name = models.CharField(max_length=40)
    Price = models.IntegerField()
    Confectionary = models.BooleanField(default = False)

    def __str__(self):
        return self.Item_name

