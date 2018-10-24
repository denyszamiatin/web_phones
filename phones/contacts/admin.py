from django.contrib import admin
from .models import Contact, PhoneNumber


class PhoneNumberAdmin(admin.TabularInline):
    model = PhoneNumber


class ContactAdmin(admin.ModelAdmin):
    list_display = 'name', 'email'
    inlines = [PhoneNumberAdmin]


admin.site.register(Contact, ContactAdmin)

admin.site.register(PhoneNumber)