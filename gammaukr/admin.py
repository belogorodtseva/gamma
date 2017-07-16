from django.contrib import admin

# Register your models here.
from gammaukr.models import Projects,Projects_steps,Models,Services,News,News_steps

admin.site.register(Projects)

admin.site.register(Models)
admin.site.register(Services)
admin.site.register(News)
admin.site.register(News_steps)


class Projects_stepsAdmin(admin.ModelAdmin):
    raw_id_fields=('project', )

admin.site.register(Projects_steps, Projects_stepsAdmin)
