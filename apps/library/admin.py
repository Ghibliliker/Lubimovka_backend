from django.contrib import admin

from apps.core.models import Role
from apps.library.forms import PerformanceAdminForm
from apps.library.models import (
    Achievement,
    Author,
    MasterClass,
    OtherLink,
    OtherPlay,
    ParticipationApplicationFestival,
    Performance,
    PerformanceMediaReview,
    PerformanceReview,
    Play,
    ProgramType,
    Reading,
    SocialNetworkLink,
    TeamMember,
)


class AuthorInline(admin.TabularInline):
    model = Author.plays.through
    extra = 1
    verbose_name = "Автор"
    verbose_name_plural = "Авторы"


class PlayAdmin(admin.ModelAdmin):
    filter_horizontal = ("authors",)
    list_display = (
        "name",
        "city",
        "program",
        "festival",
        "is_draft",
    )
    inlines = (AuthorInline,)
    list_filter = (
        "authors",
        "city",
        "program",
        "festival",
        "is_draft",
    )
    search_fields = (
        "authors__person__first_name",
        "authors__person__last_name",
        "name",
        "city",
        "program__name",
        "festival__year",
    )

    def has_change_permission(self, request, obj=None):
        return False


class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tag",
    )

    def has_change_permission(self, request, obj=None):
        return False


class AchievementInline(admin.TabularInline):
    model = Author.achievements.through
    extra = 1
    verbose_name = "Достижение"
    verbose_name_plural = "Достижения"


class PlayInline(admin.TabularInline):
    model = Author.plays.through
    extra = 1
    verbose_name = "Пьеса"
    verbose_name_plural = "Пьесы"


class SocialNetworkLinkInline(admin.TabularInline):
    model = SocialNetworkLink
    extra = 1


class SocialNetworkLinkAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


class OtherLinkInline(admin.TabularInline):
    model = OtherLink
    extra = 1


class OtherLinkAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


class OtherPlayInline(admin.StackedInline):
    model = OtherPlay
    extra = 1


class OtherPlayAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "person",
        "quote",
        "biography",
    )
    inlines = (
        AchievementInline,
        PlayInline,
        SocialNetworkLinkInline,
        OtherLinkInline,
        OtherPlayInline,
    )
    exclude = (
        "achievements",
        "plays",
        "social_network_links",
        "other_links",
        "other_plays_links",
    )
    empty_value_display = "-пусто-"

    def has_change_permission(self, request, obj=None):
        return False


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
    search_fields = (
        "media_name",
        "performance__name",
        "pub_date",
    )

    def has_change_permission(self, request, obj=None):
        return False


class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = (
        "reviewer_name",
        "performance",
        "pub_date",
    )
    list_filter = (
        "reviewer_name",
        "performance__name",
        "pub_date",
    )
    search_fields = (
        "reviewer_name",
        "performance__name",
        "pub_date",
    )

    def has_change_permission(self, request, obj=None):
        return False


class ProgramTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)

    def has_change_permission(self, request, obj=None):
        return False


class PerformanceReviewInline(admin.TabularInline):
    model = PerformanceReview
    extra = 1
    max_num = 8


class PerformanceMediaReviewInline(admin.TabularInline):
    model = PerformanceMediaReview
    extra = 1
    max_num = 8


class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    fields = (
        "person",
        "role",
    )
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Restricts role types for the model where inline is used."""
        LIMIT_ROLES = {
            Performance: "performanse_role",
            Play: "play_role",
            MasterClass: "master_class_role",
            Reading: "reading_role",
        }
        if db_field.name == "role":
            if self.parent_model in LIMIT_ROLES.keys():
                kwargs["queryset"] = Role.objects.filter(types__role_type=LIMIT_ROLES[self.parent_model])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class PerformanceAdmin(admin.ModelAdmin):
    exclude = ("events",)
    filter_horizontal = (
        "images_in_block",
        "persons",
    )
    list_filter = ("age_limit",)
    search_fields = (
        "play__name",
        "name",
        "text",
    )
    form = PerformanceAdminForm
    inlines = (
        PerformanceReviewInline,
        PerformanceMediaReviewInline,
        TeamMemberInline,
    )

    def has_change_permission(self, request, obj=None):
        return False


class ReadingAdmin(admin.ModelAdmin):
    list_display = (
        "play",
        "name",
    )
    exclude = ("events",)
    search_fields = (
        "play__name",
        "name",
    )
    inlines = (TeamMemberInline,)

    def has_change_permission(self, request, obj=None):
        return False


class MasterClassAdmin(admin.ModelAdmin):
    list_display = ("name",)
    exclude = ("events",)
    search_fields = (
        "play__name",
        "name",
    )
    inlines = (TeamMemberInline,)

    def has_change_permission(self, request, obj=None):
        return False


class OtherPlayClassAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


class ParticipationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "verified",
        "title",
        "first_name",
        "last_name",
        "city",
        "year",
        "created",
        "file",
    )
    list_filter = (
        "year",
        "verified",
        "city",
    )
    search_fields = (
        "title",
        "first_name",
        "last_name",
        "city",
        "year",
    )

    def has_change_permission(self, request, obj=None):
        return False


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "person",
        "role",
    )
    search_fields = ("role",)

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Play, PlayAdmin)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(PerformanceMediaReview, PerformanceMediaReviewAdmin)
admin.site.register(PerformanceReview, PerformanceReviewAdmin)
admin.site.register(ParticipationApplicationFestival, ParticipationAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(SocialNetworkLink, SocialNetworkLinkAdmin)
admin.site.register(OtherPlay, OtherPlayClassAdmin)
admin.site.register(OtherLink, OtherLinkAdmin)
admin.site.register(Reading, ReadingAdmin)
admin.site.register(MasterClass, MasterClassAdmin)
admin.site.register(ProgramType, ProgramTypeAdmin)
