from django.urls import path

# importing views from views..py
from views import Login
urlpatterns = [
    path('',Login),
    
] 