from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import HomeschoolApplication, Kitten


# Register your models here.

class KittenInlineTab(admin.TabularInline):
	model = Kitten
	list_display = ( 'source', 'outcome', 'name', 'description')
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
	list_display = ('application_date', 'last_name', 'first_name', 'application_status')
	inlines = [KittenInlineTab, ]
	list_filter = ['application_status', 'application_date', 'rescue_type', ]
	search_fields = ['last_name', 'first_name']

@admin.register(Kitten)
class HomeschoolApplication(admin.ModelAdmin):
	list_display = ('name', 'description', 'source', 'outcome')
	list_filter = [ 'outcome']