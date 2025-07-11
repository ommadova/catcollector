import datetime
from django.db import models
from django.urls import reverse

# Create your models here.

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField('Toy')

  def __str__(self):
    return f'{self.name} ({self.id})'
  
  def get_absolute_url(self):
    return reverse('cat-detail', kwargs={'cat_id': self.id})
  
  def fed_for_day(self):
    return self.feeding_set.filter(date=datetime.date.today()).count() >= len(MEALS)
  
class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  # Will also have a cat_id field on the feeding object
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_meal_display()} on {self.date}'
  
  class Meta:
    ordering = ['-date']
    
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})    