from django.urls import path
from .views import job_listings


urlpatterns = [

    path('',
         job_listings, name='job_listings'),
    
]