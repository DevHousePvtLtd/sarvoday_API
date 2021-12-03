from django.db import models
from django.db.models.fields import TextField
from api.categories.models import Category


class Rooms(models.Model):
    room_no = models.CharField(max_length=10)
    room_desc = models.TextField()
    room_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=200)
    capacity = models.CharField(max_length=20)
    no_of_beds = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_no
