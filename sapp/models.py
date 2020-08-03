from django.db import models

# Create your models here.


class StudentInformation(models.Model):
    id_number           = models.IntegerField(max_length=10, blank=False)
    first_name          = models.CharField(max_length=20, blank=True)
    last_name           = models.CharField(max_length=20, blank=True)
    email               =models.EmailField(max_length=25, blank=True)
    phone               = models.IntegerField(max_length=15, blank=True)
    father_name         = models.CharField(max_length=20, blank=True)
    mother_name         = models.CharField(max_length=20, blank=True)
    cgpa                = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.first_name

