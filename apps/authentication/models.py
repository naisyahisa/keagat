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
    user_email = models.ForeignKey(User, related_name='email_message', on_delete=models.SET_DEFAULT, default="anonymous")
    help_status = models.CharField(max_length=30)
    email_subject = models.CharField(max_length=50)
    email_content = models.CharField(max_length=500)
    date_created = models.DateField(auto_now = True)

    def __str__(self):
        return "{}-{}".format(self.help_status, self.user_email)