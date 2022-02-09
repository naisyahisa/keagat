from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # User deleted, the profile also deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    bg_image = models.ImageField(default= 'bgdefault.jpeg', upload_to='bg_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Helpdesk(models.Model):
    help_id = models.BigAutoField(primary_key=True)
    help_author = models.ForeignKey(User, on_delete=models.CASCADE)
    help_status = models.CharField(max_length=30)
    help_subject = models.CharField(max_length=50)
    help_content = models.CharField(max_length=500)
    date_created = models.DateField(auto_now = True)
    

    def __str__(self):
        return "{}-{}--{}-{}".format(self.help_status, self.help_author,self.help_subject, self.help_content)