from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.html import format_html


class StatusButtonMixin:
    """Mixin to add status-change buttons on page bottom."""

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = {}
        obj_class = self.model
        obj = obj_class.objects.get(pk=object_id)
        status_protected = obj.STATUS_INFO[obj.status]["special_perms"]
        extra_context["status_protected"] = status_protected
        possible_changes = obj.STATUS_INFO[obj.status]["possible_changes"]  # tuple of statuses
        statuses = {}
        for status in possible_changes:
            statuses[status] = obj.STATUS_INFO[status]
        # dict of dicts
        extra_context["possible_statuses"] = statuses
        # print(statuses)
        return super().change_view(request, object_id, form_url, extra_context)

    def response_change(self, request, obj):
        for status in obj.STATUS_INFO:
            if status in request.POST:
                obj.status = status
                obj.save()
                self.message_user(request, "Статус успешно обновлён!")
                return HttpResponseRedirect(".")
        return super().response_change(request, obj)


class DeletePermissionsMixin:
    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = {}
        obj_class = self.model
        obj = obj_class.objects.get(pk=object_id)
        if request.user.is_editor and not (obj.status == "REVIEW" or obj.status == "IN_PROCESS"):
            extra_context["show_delete"] = False
        if request.user.is_journalist and not obj.status == "IN_PROCESS":
            extra_context["show_delete"] = False
        return super().change_view(request, object_id, form_url, extra_context)


class AdminImagePreview:
    """Mixin makes preview for uploaded images.

    Need to add parameters in admin class
        list_display = ("image_preview_list_page",)
        readonly_fields = ("image_preview_change_page",)
    """

    @admin.display(description="Превью")
    def image_preview_change_page(self, obj):
        return format_html(
            '<img src="{}" width="600" height="300" style="object-fit: contain;" />'.format(obj.image.url)
        )

    @admin.display(description="Превью")
    def image_preview_list_page(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="50" style="object-fit: contain;" />'.format(obj.image.url)
            )


class HideOnNavPanelAdminModelMixin:
    """Mixin hides model from admin main page(nav. panel)."""

    def has_module_permission(self, request):
        return False
