from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Event, Acreditation, Personal, Gallery

# Admin site display settings
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.site_title = "Nat uz"
admin.site.site_header = "Nat uz"

class GalleryInLine(admin.TabularInline):
    model = Gallery
    extra = 5

    fields = (('image', "display_screenshots"),)
    readonly_fields = ("display_screenshots",)

class PersonalInLine(admin.TabularInline):
    model = Personal
    extra = 3

    fields = (('image', "display_screenshots"),)
    readonly_fields = ("display_screenshots",)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "id", 'draft')
    list_display_links = 'title',
    list_filter = ("date", "year")
    save_on_top = True
    list_editable = 'draft',
    save_as = True
    fieldsets = [
        (None, {'fields': ['title', 'description', 'date', 'url']}),
        ('Постер', {'fields': [('image', 'display_image')]}),
    ]

    readonly_fields = ("display_poster",)
    inlines = [GalleryInLine, PersonalInLine]

    def display_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='400'")

    display_image.short_description = 'Картинки'


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = 'name', 'image'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "id", 'draft')
    list_display_links = 'title',
    list_filter = ("date", "year")
    save_on_top = True
    list_editable = 'draft',
    save_as = True
    fieldsets = [
        (None, {'fields': ['title', 'description', 'date', 'url']}),
        ('Постер', {'fields': [('image', 'display_image')]}),
    ]

    readonly_fields = ("display_image",)
    inlines = [GalleryInLine, PersonalInLine]

    def display_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='400'")

    display_image.short_description = 'Картинки'

@admin.register(Acreditation)
class AcreditationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date", "email", )
    readonly_fields = ("email", "date", "name")



