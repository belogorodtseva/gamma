from django.contrib import admin

from gmsite.models import Projects,Models,Services,News,Gallery,ImageBlock,ServicesSecond,ImageGallery

admin.site.register(Models)

admin.site.register(News)




class ImageBlockInline(admin.TabularInline):
    model = ImageBlock

class ProjectsAdmin(admin.ModelAdmin):
    inlines = [
        ImageBlockInline,
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
admin.site.register(ImageBlock)

admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesSecond)

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ImageGallery)
