from django.db import models
import datetime
from datetime import date
from datetime import datetime

class Models(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=20)
    photo = models.FileField(null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Модель"
        verbose_name_plural = u"-Модели"

class Services(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=100, blank=True, null=True)
    photo = models.FileField(null=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Услуга"
        verbose_name_plural = u"-Услуги"

class Projects(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=250)
    photo = models.FileField(null=True)
    model = models.ForeignKey(Models, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Проект"
        verbose_name_plural = u"-Проекты"

class ServicesSecond(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)
    photo = models.FileField(null=False)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Подуслуга"
        verbose_name_plural = u"-Подуслуги"


class ServicesSecondPriceTable(models.Model):
    name = models.CharField(max_length=200)
    service = models.ForeignKey(ServicesSecond, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Таблица цен"
        verbose_name_plural = u"-Таблицы цен подуслуг"

class News(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=250)
    photo = models.FileField(null=True)
    model = models.ForeignKey(Models, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    active = models.BooleanField(default=True)
    video = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Новость"
        verbose_name_plural = u"-Новости"

class Gallery(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    photo = models.FileField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    model = models.ForeignKey(Models, blank=True, null=True, on_delete=models.CASCADE)
    service = models.ForeignKey(ServicesSecond, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now(), null=False, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Галерея"
        verbose_name_plural = u"-Галереи"

class ServicesSecondPriceTableElement(models.Model):
    name = models.CharField(max_length=200)
    pricefrom = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    priceto = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    notes = models.CharField(blank=True, null=True, max_length=300)
    service = models.ForeignKey(ServicesSecondPriceTable, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ServicesSecondContent(models.Model):
    text = models.TextField(blank=True, null=True)
    photo = models.FileField(blank=True, null=True)
    service = models.ForeignKey(ServicesSecond, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, blank=True, null=True, on_delete=models.CASCADE)
    news = models.ForeignKey(News, blank=True, null=True, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.text[:40]

class ImageBlock(models.Model):
   project = models.ForeignKey(Projects, on_delete=models.CASCADE)
   text = models.TextField(blank=True, null=True)
   photo1 = models.FileField(blank=True, null=True)
   photo2 = models.FileField(blank=True, null=True)

class ImageBlockNews(models.Model):
   news = models.ForeignKey(News, on_delete=models.CASCADE)
   text = models.TextField(blank=True, null=True)
   photo1 = models.FileField(blank=True, null=True)
   photo2 = models.FileField(blank=True, null=True)

class ImageGallery(models.Model):
   gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
   gimg = models.FileField(blank=True, null=True)

class Contact(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    number = models.CharField(max_length=200)
    def __str__(self):
        return self.number

    class Meta:
        verbose_name = u"Номер телефона"
        verbose_name_plural = u"-Номера телефонов"

class Links(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Ссылка"
        verbose_name_plural = u"-Ссылки на сайты"

class MainText(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    first = models.CharField(max_length=200)
    second = models.CharField(max_length=500)
    def __str__(self):
        return self.first

class Vacancy(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=200)
    money = models.CharField(max_length=300)
    contact = models.CharField(max_length=500)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Вакансия"
        verbose_name_plural = u"-Вакансии"

class NeedVacancy(models.Model):
    name = models.CharField(max_length=500)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Вопрос"
        verbose_name_plural = u"-Вопросы"

class DescriptionsProjects(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Мета-теги Проектов"
        verbose_name_plural = u"-Мета-теги Проектов"

class DescriptionsNews(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Мета-теги Новостей"
        verbose_name_plural = u"-Мета-теги Новостей"

class DescriptionsGallery(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Мета-теги Галерей"
        verbose_name_plural = u"-Мета-теги Галерей"

class DescriptionsServices(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"Мета-теги Услуг"
        verbose_name_plural = u"-Мета-теги Услуг"
