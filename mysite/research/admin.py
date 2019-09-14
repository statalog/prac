from django.contrib import admin
from .models import Study

# Register your models here.
    
class ResearchAdmin(admin.ModelAdmin):
    fieldsets = [
        ('The Basics', {'fields': ['title', 'description', 'publisher', 'contactPoint', 'mbox', 'accessLevel', 'landingPage', 'language']}),
        ('Date Info',  {'fields': ['pub_date', 'issued']}),
        ('Upload',     {'fields': ['document']}),
    ]
    
admin.site.register(Study, ResearchAdmin)
