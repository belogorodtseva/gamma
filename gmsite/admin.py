from django.contrib import admin

from gmsite.models import DescriptionsGallery,DescriptionsServices,DescriptionsProjects,DescriptionsNews,MainText,Links,Question,Vacancy,NeedVacancy,Contact,Projects,Models,Services,News,Gallery,ImageBlock,ImageBlockNews,ServicesSecond,ImageGallery,ServicesSecondContent,ServicesSecondPriceTable,ServicesSecondPriceTableElement

admin.site.register(Models)


class ImageBlockInline(admin.TabularInline):
    model = ImageBlock

class ProjectsAdmin(admin.ModelAdmin):
    inlines = [
        ImageBlockInline,
    ]

class ImageBlockNewsInline(admin.TabularInline):
    model = ImageBlockNews

class NewsAdmin(admin.ModelAdmin):
    inlines = [
        ImageBlockNewsInline,
    ]

class ServicesSecondInline(admin.TabularInline):
    model = ServicesSecond

class ServicesAdmin(admin.ModelAdmin):
    inlines = [
        ServicesSecondInline,
    ]

class ServicesSecondContentInline(admin.TabularInline):
    model = ServicesSecondContent

class ServicesSecondAdmin(admin.ModelAdmin):
    inlines = [
        ServicesSecondContentInline,
    ]

class ServicesSecondPriceTableElementInline(admin.TabularInline):
    model = ServicesSecondPriceTableElement

class ServicesSecondPriceTableAdmin(admin.ModelAdmin):
    inlines = [
        ServicesSecondPriceTableElementInline,
    ]

class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery

class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        ImageGalleryInline,
    ]

class NeedVacancyInline(admin.TabularInline):
    model = NeedVacancy

class VacancyAdmin(admin.ModelAdmin):
    inlines = [
        NeedVacancyInline,
    ]


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(ImageBlock)

admin.site.register(News, NewsAdmin)
admin.site.register(ImageBlockNews)

admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesSecond, ServicesSecondAdmin)
admin.site.register(ServicesSecondContent)

admin.site.register(ServicesSecondPriceTable, ServicesSecondPriceTableAdmin)
admin.site.register(ServicesSecondPriceTableElement)

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ImageGallery)

admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(NeedVacancy)

admin.site.register(Contact)

admin.site.register(Links)

admin.site.register(MainText)

admin.site.register(Question)

admin.site.register(DescriptionsGallery)

admin.site.register(DescriptionsNews)

admin.site.register(DescriptionsProjects)

admin.site.register(DescriptionsServices)
