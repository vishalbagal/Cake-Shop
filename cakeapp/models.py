from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cake(models.Model):
    CAT=((1,'Party Cake'),(2,'Kids Cake'),(3,'Photo Cake'),(4,'Regular Cake'),(5,'Birthday Cake'),(6,'Eggless Cake'),(7,'Anniversary Cake'))
    name=models.CharField(max_length=30,verbose_name="Product_Name")
    price=models.FloatField()
    detail=models.CharField(max_length=100,verbose_name="Product_Detail")
    cat=models.IntegerField()
    is_active=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to='image')


    def __str__(self):
        return self.name


class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    pid=models.ForeignKey(Cake,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)
    cprice=models.FloatField()


class Order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    pid=models.ForeignKey(Cake,on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)
