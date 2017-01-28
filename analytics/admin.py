from django.contrib import admin

# Register your models here.
from .models import ClickCounter

admin.site.register(ClickCounter)
