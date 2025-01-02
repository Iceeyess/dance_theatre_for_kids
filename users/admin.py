from django.contrib import admin

from users.models import User, AddressOrganization, BankAccountOrganization, Organization


# Register your models here.

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    """Класс с информацией о пользователях системы"""
    list_display = ('pk', 'email', 'username', 'phone', )
    list_display_links = ('pk', 'email', 'username', 'phone', )
    ordering = ('pk', )
    empty_value_display ='-'
    search_fields = ('email', 'username', 'phone', )
    list_filter = ('first_name', 'last_name', )

@admin.register(AddressOrganization)
class AddressOrganizationAdmin(admin.ModelAdmin):
    """Класс с информацией о адресе организации"""
    list_display = ('country', 'city', 'street', 'house', 'apartment', )
    list_display_links = ('country', 'city', 'street', 'house', 'apartment', )
    ordering = ('pk', )
    search_fields = ('country', 'city', 'street', )
    list_filter = ('country', 'city', 'street', )
    empty_value_display = '-'

@admin.register(BankAccountOrganization)
class BankAccountOrganizationAdmin(admin.ModelAdmin):
    """Класс с информацией о банке организации"""
    list_display = ('account_number', 'bic_code', 'tin_number', 'organization', )
    list_display_links = ('account_number', 'bic_code', 'tin_number', 'organization', )
    empty_value_display = '-'

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """Класс с информацией об организации"""
    list_display = ('org_name', 'phone', 'address', )
    list_display_links = ('org_name', 'phone', 'address', )
