from django.db import models

# Create your models here.

class itemsmodel(models.Model):
    img = models.ImageField(upload_to='crudapp\static')
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    price = models.CharField(max_length = 100)



class usermodel(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    contact = models.IntegerField()


