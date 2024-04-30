from django.db import models

# Create your models here.
class Emp(models.Model):
    ename=models.CharField(max_length=50)
    pno=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    add=models.CharField(max_length=50)
    
    def _str_(self):
        return self.ename