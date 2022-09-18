from django.urls import path
from .views import me, contact, about

urlpatterns = [
   path('', about),
   path('me/', me),
   path('contact/', contact),
]
