# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from .models import User


# @admin.register(User)
# class CustomAdmin(UserAdmin):

#     model = User
#     add_fieldsets = (
#         *UserAdmin.add_fieldsets,
#         (None, {'fields': ('email',)}),
#         ('Personal info', {'fields': (('first_name', 'last_name', 'patronymic'),
#                                       'birth_date', 'sex', 'phone_number',)}),
#         ('Comment', {'fields': ('comment',)}),
#         ('Role', {'fields': ('role',)}),
#     )

#     fieldsets = (
#         *UserAdmin.fieldsets,
#         ('Role', {'fields': ('role',)}),
#     )

#     list_display = [
#         'username',
#         'email',
#         'first_name',
#         'patronymic',
#         'last_name',
#         'birth_date',
#         'sex',
#         'phone_number',
#         'role',
#     ]


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):

    list_display = [
        'username',
        'email',
        'first_name',
        'patronymic',
        'last_name',
        'birth_date',
        'sex',
        'phone_number',
        'role',
    ]
    list_filter = ('role', 'sex',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username',)}),
        ('Personal info', {'fields': (('first_name', 'last_name', 'patronymic'),
                                      'birth_date', 'sex', 'phone_number',)}),
        ('Comment', {'fields': ('comment',)}),
        ('Role', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username',),
        }),
        ('Personal info', {'fields': (('first_name', 'last_name', 'patronymic'),
                                      'birth_date', 'sex', 'phone_number',)}),
        ('Comment', {'fields': ('comment',)}),
        ('Role', {'fields': ('role',)}),
    )
    search_fields = ('email', 'username', 'first_name',
                     'last_name', 'patronymic',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
