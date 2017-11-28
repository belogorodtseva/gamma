from django.db import models

class Models(models.Model):
    name = models.CharField(max_length=20)
    photo = models.FileField(null=False)

    def __str__(self):
        return self.name

class Services(models.Model):
    name = models.CharField(max_length=50)
    photo = models.FileField(null=False)
    def __str__(self):
        return self.name

class ServicesSecond(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)
    photo = models.FileField(null=False)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField(blank=True, null=True)
    photo = models.FileField(null=True)
    model = models.ForeignKey(Models, blank=True, null=True)
    service = models.ForeignKey(Services, blank=True, null=True)
    start = models.BooleanField(default=False)
    top = models.BooleanField(default=False)

    def __str__(self):
        startkey = ""
        topkey = ""
        if (self.start == True):
            startkey += "| НА ГЛАВНОЙ"
        if (self.top == True):
            topkey += "| ПОДНЯТЬ ВВЕРХ"

        return '%s...  %s   %s ' % (str(self.name)[:40], startkey, topkey)


class News(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField(blank=True, null=True)
    photo = models.FileField(null=True)
    model = models.ForeignKey(Models, blank=True, null=True)
    service = models.ForeignKey(Services, blank=True, null=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):

    name = models.CharField(max_length=250, blank=True, null=True)
    photo = models.FileField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Image(models.Model):
   project = models.ForeignKey(Projects, on_delete=models.CASCADE)
   photo = models.FileField(blank=True, null=True)
   text = models.TextField(blank=True, null=True)

class ImageGallery(models.Model):

   gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
   gimg = models.FileField(blank=True, null=True)


class HomePhoto(models.Model):

    photo = models.FileField(blank=True, null=True)
