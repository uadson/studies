from django.db import models


class Base(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Car(Base):
    model = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)
    year = models.IntegerField()

    class Meta:
        ordering = ['-created']
