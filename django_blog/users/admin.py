from django.contrib import admin
from .models import Profile, Follow


admin.site.register((Profile, Follow))
