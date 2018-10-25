from django.urls import path
from .views import info, add_contact, add_number


urlpatterns = [
    path('info/<int:contact_id>', info),
    path('add', add_contact),
    path('add_number/<int:contact_id>', add_number),
]