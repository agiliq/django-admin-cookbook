from django.contrib import admin
from django.db.models import Count

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

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _hero_count=Count("hero", distinct=True),
            _villain_count=Count("villain", distinct=True),
        )
        return queryset

    def hero_count(self, obj):
        return obj._hero_count

    def villain_count(self, obj):
        return obj._villain_count
