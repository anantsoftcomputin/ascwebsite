from django.contrib import admin
from testing_app.models import User
from testing_app.models import Contact
from testing_app.models import Job

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Job)