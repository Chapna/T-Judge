from django.contrib import admin

from .models import Submit
from .models import Problem
from .models import Homework

# Register your models here.
admin.site.register(Submit)
admin.site.register(Problem)
admin.site.register(Homework)
