from django.db import models


# Create your models here.
seller_choices = (
    ('Flipkart','Flipkart'),
    ('Amazon','Amazon'),
    ('Myntra','Mynta'),
    ('Ebay','Ebay'),

)
class Customer1(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Orders(models.Model):
    customer = models.ForeignKey(Customer1, on_delete=models.CASCADE)
    prod_id = models.IntegerField()
    p_name = models.CharField(max_length=30)
    p_price = models.FloatField()
    p_seller = models.CharField(max_length=20, choices=seller_choices)

    def __str__(self):
        return self.p_name