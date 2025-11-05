from django.db import models

# Create your models here.

class CustomerData(models.Model):
    customer_fullname = models.CharField(max_length=255)
    customer_email = models.EmailField(unique=True)
    customer_phone = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=500)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_fullname
    
class InvoiceData(models.Model):
    pass

