from django.contrib import admin
from django.contrib.auth.models import User # Import the built-in User model

# If you had custom models in auth_app/models.py, you would register them here.
# For example, if you had a UserProfile model:
# from .models import UserProfile
# admin.site.register(UserProfile)

# Django's built-in User model is already registered by default,
# but you can customize its admin view if needed.
# For this basic setup, no explicit registration is needed for User,
# unless you want to create a custom UserAdmin.

