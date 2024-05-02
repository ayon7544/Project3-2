from django.contrib import admin
from .models import *


admin.site.register(Medicine)
admin.site.register(Book)

admin.site.register(Symptom)
admin.site.register(Disease)
