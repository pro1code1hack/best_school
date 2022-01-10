from django.contrib import admin

from .models import Question, Answer, Result, Quiz

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