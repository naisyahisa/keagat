from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vaksinasi(models.Model):
    id = models.BigAutoField(primary_key=True)
    district = models.CharField(max_length=30)
    year = models.IntegerField()
    vac_able = models.IntegerField()
    vac_done = models.IntegerField()
    
    def __str__(self):
        return "{}-{}-{}-{}".format(self.district, self.year, self.vac_able, self.vac_done)


#class = table, attribute = fields
class Post(models.Model):
    #field, with restriction
    title = models.CharField(max_length=100)
    #lines of text no restr.
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #passed in the user table, on-delete if the user got deleted, also posts got deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #to print out db, dunder method, charfield
    def __str__(self):
        return self.title 