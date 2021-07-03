
from django.db import models

class product(models.Model):
        def __str__(self):
            return self.name
        name=models.CharField(max_length=50)
        des=models.CharField(max_length=50)
        img=models.ImageField(upload_to='picture')

