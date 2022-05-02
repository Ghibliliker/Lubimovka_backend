from django.contrib import admin

from apps.library.models import PerformanceMediaReview


@admin.register(PerformanceMediaReview)
class PerformanceMediaReviewAdmin(admin.ModelAdmin):
    list_display = (
        "media_name",
        "performance",
        "pub_date",
    )
    list_filter = (
        "media_name",
        "performance__name",
        "pub_date",
    )
    autocomplete_fields = ("performance",)
    search_fields = (
        "media_name",
        "performance__name",
        "pub_date",
    )
    readonly_fields = ("pub_date",)
