from django.contrib import admin
from .models import Vaksinasi
from .models import Post

# Register your models here.

admin.site.register(Vaksinasi)
admin.site.site_header = 'Keagat Administration'
admin.site.register(Post)


