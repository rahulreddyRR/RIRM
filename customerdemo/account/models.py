from django.db import models

# Create your models here.
class customerinfo(models.Model):
    FullName = models.CharField(blank=False, max_length=100)
    Phonenumber = models.IntegerField(blank=False,unique=True)
    Client_Value = models.DecimalField(max_digits=19, decimal_places=2)
    Email = models.EmailField()
    protfolio_site = models.URLField(blank=True)

    def __str__(self):
        return self.FullName
