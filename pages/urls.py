from django.urls import path
from .views import home, fetch_member, register_member

urlpatterns = [
   path('', home, name='home'),  # 👈 Add this line
   path('api/fetch/', fetch_member, name='fetch_member'),
    path('api/register/', register_member, name="register_member"),
    
    
]