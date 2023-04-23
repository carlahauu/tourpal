from django.contrib import admin
from django.urls import path
from .views import landing
from . import views 

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.landing, name="home"), 
  path('guide', views.bot, name="guide")
]