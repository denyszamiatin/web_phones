from django.urls import path
from .views import index, info, add_contact, add_number


urlpatterns = [
    path('', index),
    path('info/<int:contact_id>', info),
    path('add', add_contact),
    path('add_number/<int:contact_id>', add_number),
]