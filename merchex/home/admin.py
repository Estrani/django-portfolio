from django.contrib import admin
from home.models import FirstPage
from home.block import JourneyBanner

admin.site.register(FirstPage)
admin.site.register(JourneyBanner)

