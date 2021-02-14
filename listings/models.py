from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    address = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=10)
    price = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return '%s object (%s, %s, %s)' % (self.__class__.__name__, self.pk, self.title, self.price)
