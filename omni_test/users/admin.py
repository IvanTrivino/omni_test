# Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models imports
from omni_test.users.models import User


admin.site.register(User, UserAdmin)
