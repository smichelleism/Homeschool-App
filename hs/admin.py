from django.contrib import admin
from .models import HomeschoolApplication, Kitten


# Register your models here.

class KittenInline(admin.StackedInline):
	model = Kitten
	extra = 0


@admin.register(HomeschoolApplication)
class HomeschoolApplication(admin.ModelAdmin):
	list_display = ('application_date', 'last_name', 'first_name')
	inlines = [KittenInline, ]
	list_filter = ['application_date', 'rescue_type', ]

@admin.register(Kitten)
class HomeschoolApplication(admin.ModelAdmin):
	list_display = ('name', 'description', 'outcome')