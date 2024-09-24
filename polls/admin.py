from django.contrib import admin

from .models import Question, Choice

# Register your models here.

class ChoiceAdmin(admin.ModelAdmin):
    question = "question"
    text = "choice_text"

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2
    exclude=["votes"]

class QuestionAdmin(admin.ModelAdmin):
    question = "question_text"
    date_published = "pub_date"   
    inlines=[ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)