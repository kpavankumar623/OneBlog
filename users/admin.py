from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth.models import User

from .models import UserProfile

#####inlines = (UserProfileInline,)

#admin.site.unregister(User)
admin.site.register(UserProfile)
