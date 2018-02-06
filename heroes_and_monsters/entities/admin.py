from django.contrib import admin

from .models import Hero, Villain, Category, Origin

admin.site.register(Villain)


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "is_immortal", "category", "origin")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = ("name", "hero_count", "villain_count")


    def hero_count(self, obj):
        return obj.hero_set.count()

    def villain_count(self, obj):
        return obj.villain_set.count()
