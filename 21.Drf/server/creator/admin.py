from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from creator.models import Author

admin.site.register(Author)
