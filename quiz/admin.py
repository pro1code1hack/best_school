from django.contrib import admin

from lessons.models import Topic
from .models import Question, Answer, Result, Quiz , AnswerType, ResultMistake

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

# Register your models here.

class ResultAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'user', 'score',)

admin.site.register(Result, ResultAdmin)

admin.site.register(Quiz)

admin.site.register(AnswerType)

admin.site.register(ResultMistake)

admin.site.register(Topic)