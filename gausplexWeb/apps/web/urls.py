from .views import Index
from django.urls import path, include

app_name = 'website'

urlpatterns = [
    path('', Index.as_view(), name="index"),
]
