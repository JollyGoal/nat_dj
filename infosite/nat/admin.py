from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post, Acreditation, Personal, Gallery, Category, Files, Contact, Text, Sponsor, Image


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

class TextAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Text
        fields = '__all__'


class FilesAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Files
        fields = '__all__'


# Admin site display settings
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.site_title = "Nat uz"
admin.site.site_header = "Nat uz"

class SponsorInLine(admin.TabularInline):
    model = Sponsor
    extra = 1
    fields = (('title', 'images', 'url', 'display_logo'),)
    readonly_fields = ("display_logo",)

    def display_logo(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='400'")

    display_logo.short_description = 'Логотип'

class ImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = (('image', "display_img"),)
    readonly_fields = ("display_img",)

    def display_img(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='400'")

    display_img.short_description = 'Картинки'

class GalleryInLine(admin.TabularInline):
    model = Gallery
    extra = 1

    fields = (('name', 'image', "display_screenshots"),)
    readonly_fields = ("display_screenshots",)

    def display_screenshots(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='400'")

    display_screenshots.short_description = 'Скриншот'

class PersonalInLine(admin.TabularInline):
    model = Personal
    extra = 1

    fields = (( 'title', 'description', 'perscat', 'image', "display_persons"),)
    readonly_fields = ("display_persons",)

    def display_persons(self, obj):
        return mark_safe(f"<img src={obj.image.url} height='400'")

    display_persons.short_description = 'Скриншот'

class FilesInLine(admin.TabularInline):
    model = Files
    extra = 1
    form = FilesAdminForm

    fields = ('title', 'description', 'file')

class TextInLinedmin(admin.TabularInline):
    model = Text
    extra = 1
    form = TextAdminForm

    fields = ('title', 'description',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ("title", "date", "id", 'draft', 'category')
    list_display_links = 'title',
    list_filter = ("date",)
    save_on_top = True
    list_editable = 'draft',
    form = PostAdminForm
    save_as = True
    fieldsets = [
        (None, {'fields': ['title', 'description', 'date', 'category', 'url']}),
        ('Image', {'fields': [('poster', 'display_poster')]}),
    ]
    readonly_fields = ("display_poster",)
    inlines = [TextInLinedmin, FilesInLine, GalleryInLine, PersonalInLine, SponsorInLine, ImageInLine]

    def display_poster(self, obj):
        return mark_safe(f"<img src={obj.poster.url} height='400'")

    display_poster.short_description = 'Главная картинка'


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = 'title', 'id', 'perscat',
    list_display_links = 'title',

@admin.register(Files)
class FileslAdmin(admin.ModelAdmin):
    list_display = 'title', 'id',
    list_display_links = 'title',
    form = FilesAdminForm
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = 'name', 'id',
    list_display_links = 'name',

# @admin.register(Text)
# class TextAdmin(admin.ModelAdmin):
#     list_display = 'title', 'id',
#     list_display_links = 'title',
#     form = TextAdminForm

@admin.register(Acreditation)
class AcreditationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date", "email", )
    readonly_fields = ("email", "date", "name", "files", "format", "phone", "info", "list", "title")
    list_display_links = 'name',
    list_filter = ("date",)

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = 'title', 'id',
    list_display_links = 'title',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'id',

# @admin.register(Files)
# class FileslAdmin(admin.ModelAdmin):
#     list_display = 'title', 'id',
#     list_display_links = 'title',
# list_display_links = 'name',

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date", "email", )
    readonly_fields = ("email", "date", "title", "files", "message", "phone", "face")
    list_display_links = 'title',
    list_filter = ("date",)



