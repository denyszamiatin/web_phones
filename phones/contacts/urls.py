from django.urls import path
from .views import info, add_contact


urlpatterns = [
    path('info/<int:contact_id>', info),
    path('add', add_contact)
]