from django.contrib import admin

from Moneybudget.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(Category)