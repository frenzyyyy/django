from django.contrib import admin

# Register your models here.
from .models import Test
from .models import Choice
from .models import Question
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(Choice)