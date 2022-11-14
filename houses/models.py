from django.db import models

class House(models.Model):
    name = models.CharField('name', max_length=50)
    price = models.IntegerField('price')
    description = models.TextField('description')
    image = models.ImageField('image', upload_to='houses\images', default='', blank=True)

    class Meta:
        verbose_name = 'house'
        verbose_name_plural = 'houses'
        ordering = ["name"]

    def __str__(self):
        return self.name.upper()