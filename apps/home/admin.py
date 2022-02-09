# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Vaksinasi
# Register your models here.

admin.site.register(Vaksinasi)
admin.site.site_header = 'Keagat Administration'
