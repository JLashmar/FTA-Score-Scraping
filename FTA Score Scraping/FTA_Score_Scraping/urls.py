"""
Definition of urls for FTA_Score_Scraping.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
from django.urls import path
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]
