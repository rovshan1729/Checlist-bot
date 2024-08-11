from django.contrib.admin import ModelAdmin, register
from . import models

@register(models.TelegramProfile)
class TelegramProfileAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 
                    'username')
    list_display_links = ('id', 'username')
    

@register(models.Section)
class SectionAdmin(ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    

@register(models.Question)
class QuestionAdmin(ModelAdmin):
    list_display = ('id', 'title', 
                    'section', 'order')
    list_display_links = ('id', 'title')
    ordering = ('id',)
    