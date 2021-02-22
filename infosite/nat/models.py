from django.db import models
from django.utils.text import slugify
from datetime import date


class Personal(models.Model):
    """ПЕРСОНАЛ"""
    name = models.CharField("Имя", max_length=100, blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="people/")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"

class News(models.Model):
    """НОВОСТИ"""
    title = models.CharField("Оглавление", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Главная Картинка", upload_to="images/")
    date = models.DateTimeField("Дата", auto_now_add=True)
    shots = models.ImageField("Картинки", upload_to="shots/")
    url = models.SlugField(max_length=160, unique=True, blank=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.url = slugify(self.title, allow_unicode=True) + '-' + str(self.id)
        super().save(update_fields=['url'])

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"



class Event(models.Model):
    """МЕРОПРИЯТИЯ"""
    title = models.CharField("Оглавление", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Главная Картинка", upload_to="images/")
    date = models.DateTimeField("Дата", auto_now_add=True)
    url = models.SlugField(max_length=160, unique=True, blank=True)
    draft = models.BooleanField("Черновик", default=False)
    personal = models.ForeignKey(Personal, verbose_name="Персонал", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.url = slugify(self.title, allow_unicode=True) + '-' + str(self.id)
        super().save(update_fields=['url'])

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class Gallery(models.Model):
    image = models.ImageField("Главная Картинка", upload_to="gallery/")
    date = models.DateTimeField("Дата", auto_now_add=True, blank=True, null=True, default='')
    event = models.ForeignKey(Event, verbose_name="Мероприятие", on_delete=models.CASCADE, blank=True, null=True)
    news = models.ForeignKey(News, verbose_name="Новости", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = "Галлерея"
        verbose_name_plural = "Галлерея"

class Acreditation(models.Model):
    title = models.CharField("Аккредитация", max_length=150)
    format = models.CharField("Формат выхода материала", max_length=150)
    name = models.CharField("Ф.И.О.", max_length=150)
    date = models.DateTimeField("Дата выхода материала", auto_now_add=True)
    email = models.EmailField("E-mail")
    phone = models.PositiveSmallIntegerField("Телефон", blank=True, null=True, help_text="+998")
    info = models.TextField("Информация")
    list = models.TextField("Список съемочного оборудования")
    files = models.FileField("Файлы", upload_to="materials/", null=False, blank=False)


