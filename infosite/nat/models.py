from django.db import models


class Category(models.Model):
    name = models.CharField("Категории", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Post(models.Model):
    """НОВОСТИ И МЕРОПРИЯТИЯ"""
    title = models.CharField("Оглавление", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Главная Картинка", upload_to="images/")
    date = models.DateTimeField("Дата")
    category = models.ForeignKey(Category, verbose_name="Категория",
                                 on_delete=models.SET_NULL, null=True)

    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return str(self.title)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.url = slugify(self.category, allow_unicode=True) + '-' + str(self.id)
    #     super().save(update_fields=['url'])

    class Meta:
        verbose_name = "Новости и Мероприятия"
        verbose_name_plural = "Новости и Мероприятия"

class Files(models.Model):
    title = models.CharField("Оглавление", max_length=150)
    description = models.TextField("Описание файла", blank=True, null=True)
    file = models.FileField("Документы (PDF, WORD...)", upload_to="files/")
    documents = models.ForeignKey(Post, verbose_name="Документы к",
                                 on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

class Gallery(models.Model):
    name = models.CharField("Название", max_length=100)
    image = models.ImageField("Фото Галлерея", upload_to="gallery/")
    gallery = models.ForeignKey(Post, verbose_name="Новости и Мероприятия",
                              on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Галлерея"
        verbose_name_plural = "Галлерея"

class Text(models.Model):
    title = models.CharField("Оглавление", max_length=150)
    description = models.TextField("Описание")
    add = models.ForeignKey(Post, verbose_name="Дополнительная информация",
                              on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Дополнительный текст"
        verbose_name_plural = "Дополнительный текст"


class Personal(models.Model):
    """ПЕРСОНАЛ"""
    title = models.CharField("Краткая информация", max_length=500)
    image = models.ImageField("Изображение", upload_to="people/")
    personal = models.ForeignKey(Post, verbose_name="Персонал",
                                 on_delete=models.CASCADE, blank=True, null=True)
    perscat = models.ForeignKey(Category, verbose_name="",
                              on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"

class Acreditation(models.Model):

    title = models.CharField("Название СМИ", max_length=150)
    format = models.CharField("Формат выхода материала", max_length=150)
    name = models.CharField("Ф.И.О.", max_length=150)
    date = models.DateTimeField("Дата выхода материала")
    email = models.EmailField("E-mail")
    phone = models.PositiveSmallIntegerField("Телефон", blank=True, null=True, help_text="+998")
    info = models.TextField("Информация")
    list = models.TextField("Список съемочного оборудования")
    files = models.FileField("Файлы", upload_to="materials/", null=False, blank=False)

    def __str__(self):
        return f"{self.title} - {self.name}"

    class Meta:
        verbose_name = "Аккредитация"
        verbose_name_plural = "Аккредитации"


class Contact(models.Model):

    title = models.CharField("Наименование организации", max_length=150)
    face = models.CharField("Контактное лицо", max_length=150)
    phone = models.PositiveSmallIntegerField("Телефон", blank=True, null=True, help_text="+998")
    date = models.DateTimeField("Дата выхода материала", auto_now_add=True)
    email = models.EmailField("E-mail")
    message = models.TextField("Сообщение")
    files = models.FileField("Файлы", upload_to="contact/", null=False, blank=False)

    def __str__(self):
        return f"{self.title} - {self.face}"

    class Meta:
        verbose_name = "Связь с нами"
        verbose_name_plural = "Связь с нами"

