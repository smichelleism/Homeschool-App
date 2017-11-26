from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import HomeschoolApplication, Kitten


# Register your models here.

class KittenInlineTab(admin.TabularInline):
	model = Kitten
	list_display = ( 'name', 'description')
	extra = 0
	formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'10'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':40})},
    }

class KittenInline(admin.StackedInline):
	model = Kitten
	extra = 0


@admin.register(HomeschoolApplication)
class HomeschoolApplication(admin.ModelAdmin):
	list_display = ('application_date', 'last_name', 'first_name')
	inlines = [KittenInlineTab, ]
	list_filter = ['application_date', 'rescue_type', ]

@admin.register(Kitten)
class HomeschoolApplication(admin.ModelAdmin):
	list_display = ('name', 'description', 'outcome')
	list_filter = [ 'outcome']