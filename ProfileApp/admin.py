from django.contrib import admin

# Register your models here.
from .models import Profile 

class ProfileAtt(admin.ModelAdmin):
    list_display=['firstName','lastName','gmail']

admin.site.register(Profile,ProfileAtt)