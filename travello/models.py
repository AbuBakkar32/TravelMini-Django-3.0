from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='None')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "city"

