from django.db import models

# Create your models here.
class InvGen(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company_name =  models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    conf_password = models.CharField(max_length=100)
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email