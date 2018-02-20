from django.contrib import admin
from django.db.models import Count

from .models import Hero, Villain, Category, Origin, HeroProxy

import csv
import sys
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.urls import path


class IsVeryBenevolentFilter(admin.SimpleListFilter):
    title = 'is_very_benevolent'
    parameter_name = 'is_very_benevolent'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(benevolence_factor__gt=75)
        elif value == 'No':
            return queryset.exclude(benevolence_factor__gt=75)
        return queryset


class ExportCsvMixin:

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name", "is_immortal", "category", "origin", "is_very_benevolent")
    list_filter = ("is_immortal", "category", "origin", IsVeryBenevolentFilter)
    actions = ["mark_immortal"]

    exclude = ['added_by',]

    # fields = ["headshot_image"]

    readonly_fields = ["headshot_image"]

    change_list_template = "entities/heroes_changelist.html"

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
            )
    )

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         return ["name", "category"]
    #     else:
    #         return []

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('immortal/', self.set_immortal),
            path('mortal/', self.set_mortal),
        ]
        return my_urls + urls

    def set_immortal(self, request):
        self.model.objects.all().update(is_immortal=True)
        self.message_user(request, "All heroes are now immortal")
        return HttpResponseRedirect("../")

    def set_mortal(self, request):
        self.model.objects.all().update(is_immortal=False)
        self.message_user(request, "All heroes are now mortal")
        return HttpResponseRedirect("../")

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.added_by = request.user
        super().save_model(request, obj, form, change)


    def mark_immortal(self, request, queryset):
        queryset.update(is_immortal=True)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def is_very_benevolent(self, obj):
        return obj.benevolence_factor > 75


    # def has_add_permission(self, request):
    #     return has_hero_access(request.user)

    # def has_change_permission(self, request, obj=None):
    #     return has_hero_access(request.user)

    # def has_delete_permission(self, request, obj=None):
    #     return has_hero_access(request.user)

    # def has_module_permission(self, request):
    #     return has_hero_access(request.user)


    is_very_benevolent.boolean = True


@admin.register(HeroProxy)
class HeroProxyAdmin(admin.ModelAdmin):
    list_display = ("name", "is_immortal", "category", "origin",)
    readonly_fields = ("name", "is_immortal", "category", "origin",)



@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ("name", "category", "origin")
    actions = ["export_as_csv"]

    readonly_fields = ["added_on"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    list_display = ("name", "hero_count", "villain_count")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

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

    hero_count.admin_order_field = '_hero_count'
    villain_count.admin_order_field = '_villain_count'
