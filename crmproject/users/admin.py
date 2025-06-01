from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Order
from .forms import CustomUserCreationForm
from auditlog.models import LogEntry
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'user_type', 'phone', 'address')}),
        ('Permissions', {'fields': ('is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'user_type', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'customer', 'amount', 'status', 'created_at')

# admin.site.register(LogEntry)