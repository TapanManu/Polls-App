from django.contrib import admin
from . models import Question,Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
	model=Choice
	extra=3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets=[
		('Question Text',{'fields':['question_text']}),
		('Published Date',{'fields':['date_published'],'classes':['collapse']}),
		]
	inlines=[ChoiceInline]	

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

