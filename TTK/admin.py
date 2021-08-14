from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header='TeamTechKenya'
admin.site.register(CONTACT)
admin.site.register(DIRECTORS)
admin.site.register(PROJECT)