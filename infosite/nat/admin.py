from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Acreditation, Personal, Gallery, Category, Files

# Admin site display settings
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.site_title = "Nat uz"
admin.site.site_header = "Nat uz"

class GalleryInLine(admin.TabularInline):
    model = Gallery
    extra = 1

    fields = (('image', "display_screenshots"),)
    readonly_fields = ("display_screenshots",)

    def display_screenshots(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='400'")

    display_screenshots.short_description = 'Скриншот'

class PersonalInLine(admin.TabularInline):
    model = Personal
    extra = 1

    fields = (('title', 'image', "display_persons"),)
    readonly_fields = ("display_persons",)

    def display_persons(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='400'")

    display_persons.short_description = 'Скриншот'

class FilesInLine(admin.TabularInline):
    model = Files
    extra = 1

    fields = ('name', 'file',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "id", 'draft', 'category')
    list_display_links = 'title',
    list_filter = ("date",)
    save_on_top = True
    list_editable = 'draft',
    save_as = True
    fieldsets = [
        (None, {'fields': ['title', 'description', 'date', 'category', 'url']}),
        ('Image', {'fields': [('image', 'display_image')]}),
    ]
    readonly_fields = ("display_image",)
    inlines = [FilesInLine , GalleryInLine, PersonalInLine]

    def display_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='400'")

    display_image.short_description = 'Картинки'


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = 'title', 'id',
    list_display_links = 'title',

@admin.register(Files)
class FileslAdmin(admin.ModelAdmin):
    list_display = 'name', 'id',
    list_display_links = 'name',

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = 'name', 'id',
    list_display_links = 'name',


@admin.register(Acreditation)
class AcreditationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date", "email", )
    readonly_fields = ("email", "date", "name", "files", "format", "phone", "info", "list", "title")
    list_display_links = 'name',
    list_filter = ("date",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'id',
    list_display_links = 'name',



