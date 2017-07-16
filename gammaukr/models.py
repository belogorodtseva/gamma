from django.db import models

# Create your models here.
class Models(models.Model):
    name = models.CharField(max_length=20)
    photo = models.FileField(null=False)

    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=20)
    photo = models.FileField(null=False)
    text = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()
    photo = models.FileField(null=True)
    model = models.ForeignKey(Models, blank=True, null=True)
    service = models.ForeignKey(Services, blank=True, null=True)

    def __str__(self):
        return self.name


class Projects_steps(models.Model):
    project = models.ForeignKey(Projects)
    step_num = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    photo = models.FileField(blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (str(self.step_num), str(self.project))

class News(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField(blank=True, null=True)
    photo = models.FileField(null=True)
    model = models.ForeignKey(Models, blank=True, null=True)
    service = models.ForeignKey(Services, blank=True, null=True)

    def __str__(self):
        return self.name


class News_steps(models.Model):
    news = models.ForeignKey(News)
    step_num = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    photo = models.FileField(blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (str(self.step_num), str(self.news))
