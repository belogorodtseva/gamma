from django.contrib import admin

from gmsite.models import Projects,Models,Services,News,Gallery,Image,ServicesSecond,ImageGallery,HomePhoto

admin.site.register(Models)

admin.site.register(News)

admin.site.register(HomePhoto)


class ImageInline(admin.TabularInline):
    model = Image

class ProjectsAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

class ServicesSecondInline(admin.TabularInline):
    model = ServicesSecond

class ServicesAdmin(admin.ModelAdmin):
    inlines = [
        ServicesSecondInline,
    ]

class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery

class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        ImageGalleryInline,
    ]


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Image)

admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesSecond)

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ImageGallery)
