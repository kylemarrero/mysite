from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class TutorialAdmin(admin.ModelAdmin):

	fieldsets = [
		("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
		("Content", {"fields":["tutorial_content"]})
	]

	formfields_overrides = {
		models.TextField: {'widet': TinyMCE()}
	}

admin.site.register(Tutorial, TutorialAdmin)