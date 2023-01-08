from django.contrib import admin
from . models import City, Language, Vacancy, Error, Url

# Register your models here.

class VacancyAdmin(admin.ModelAdmin):
	list_display = ('title', 'company', 'language', 'timestamp')
	list_display_links = ('title',)
	search_fields = ('title', 'company')


admin.site.register(City)
admin.site.register(Language)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Error)
admin.site.register(Url)
