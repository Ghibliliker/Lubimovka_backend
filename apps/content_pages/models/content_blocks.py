from django.contrib import admin
from django.db import models
from django.db.models.constraints import UniqueConstraint

from apps.content_pages.models import AbstractItemWithTitle
from apps.core.models import BaseModel, Person, Role
from apps.library.models import Performance, Play

from ..models.content_block_items import AbstractContentBlockItem


class OrderedPerformance(AbstractContentBlockItem):
    item = models.ForeignKey(
        Performance,
        on_delete=models.CASCADE,
        related_name="ordered_performances",
        verbose_name="Спектакль",
    )
    block = models.ForeignKey(
        "PerformancesBlock",
        on_delete=models.CASCADE,
        related_name="ordered_performances",
    )


class ContentPersonRole(BaseModel):
    extended_person = models.ForeignKey(
        "ExtendedPerson",
        on_delete=models.CASCADE,
        related_name="content_person_roles",
        verbose_name="Персона",
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="content_person_roles",
        verbose_name="Роль",
    )

    def __str__(self):
        return self.role.name

    class Meta:
        verbose_name = "Роль у персоны в блоке"
        verbose_name_plural = "Роли персон в блоках"
        constraints = (
            UniqueConstraint(
                fields=(
                    "extended_person",
                    "role",
                ),
                name="unique_role_per_extended_person",
            ),
        )


class ExtendedPerson(AbstractContentBlockItem):
    """Extended `Person` for `personsblock`.

    Person extended not only with `order` but also with `roles`.
    """

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="extended_persons",
        verbose_name="Персона/человек",
    )
    roles = models.ManyToManyField(
        Role,
        through=ContentPersonRole,
        related_name="extended_persons",
        verbose_name="Роли персоны",
    )
    block = models.ForeignKey(
        "PersonsBlock",
        on_delete=models.CASCADE,
        related_name="extended_persons",
        verbose_name="Блок персон",
    )

    class Meta:
        ordering = ("order",)
        verbose_name = "Элемент блока персон"
        verbose_name_plural = "Элементы блоков песроны"
        constraints = (
            UniqueConstraint(
                fields=(
                    "block",
                    "person",
                ),
                name="unique_person_per_block",
            ),
        )

    def __str__(self):
        return f"{self.order} — {self.person}"

    @admin.display(description="Роли")
    def person_roles(self):
        if self.roles.exists():
            roles = ", ".join([role.name for role in self.roles.all()])
        else:
            roles = "не установлено"
        return roles


class OrderedPlay(AbstractContentBlockItem):
    item = models.ForeignKey(
        Play,
        on_delete=models.CASCADE,
        related_name="ordered_plays",
        verbose_name="Пьеса",
    )
    block = models.ForeignKey(
        "PlaysBlock",
        on_delete=models.CASCADE,
        related_name="ordered_plays",
    )


class OrderedVideo(AbstractContentBlockItem):
    title = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Заголовок",
        help_text="Заголовок/подпись для видео. Может быть пустым",
    )
    url = models.URLField(
        verbose_name="Ссылка на видео",
    )
    block = models.ForeignKey(
        "VideosBlock",
        on_delete=models.CASCADE,
        related_name="ordered_videos",
    )

    def __str__(self):
        return f"Видео {self.order}"


class ImagesBlock(AbstractItemWithTitle):
    """Model to store and organize OrderedContentImagesBlockItems objects."""

    class Meta:
        verbose_name = "Блок изображения"
        verbose_name_plural = "Блоки изображений"


class PerformancesBlock(AbstractItemWithTitle):
    items = models.ManyToManyField(
        to=Performance,
        through=OrderedPerformance,
        related_name="performance_blocks",
    )

    class Meta:
        verbose_name = "Блок спектаклей"
        verbose_name_plural = "Блоки спектаклей"


class PersonsBlock(AbstractItemWithTitle):
    items = models.ManyToManyField(
        to=Person,
        through=ExtendedPerson,
        related_name="person_blocks",
    )

    class Meta:
        verbose_name = "Блок персон"
        verbose_name_plural = "Блоки персон"


class PlaysBlock(AbstractItemWithTitle):
    items = models.ManyToManyField(
        to=Play,
        through=OrderedPlay,
        related_name="play_blocks",
    )

    class Meta:
        verbose_name = "Блок пьес"
        verbose_name_plural = "Блоки пьес"


class VideosBlock(AbstractItemWithTitle):
    """Model to store and organize OrderedVideos objects."""

    class Meta:
        verbose_name = "Блок видео"
        verbose_name_plural = "Блоки видео"
