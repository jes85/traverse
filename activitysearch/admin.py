from django.contrib import admin

# Register your models here.
from activitysearch.models import Trip, Activity, Location

admin.site.register(Trip)
admin.site.register(Activity)
admin.site.register(Location)
