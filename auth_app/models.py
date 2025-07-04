from django.db import models

# Example: If you wanted to extend the User model with additional profile fields,
# you would typically do it here using a OneToOneField relationship.
# However, for a basic session-based authentication, this file can remain
# empty or just contain the necessary imports.

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return self.user.username


