from django.contrib import admin

from .models import Hero, Villain, Category, Origin

admin.site.register(Hero)
admin.site.register(Villain)
admin.site.register(Category)
admin.site.register(Origin)
