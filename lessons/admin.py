from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms

from .models import Lesson


# admin.site.register(Lesson)
# admin.site.register(Lesson_Video)


class LessonAdminForm(forms.ModelForm):
    """
    # this form allows us to configure which form will be edited via CKE editor
    """
    ch_lesson_text = forms.CharField(label ='Текст урока', widget=CKEditorWidget())
    ch_lesson_plan = forms.CharField(label ='План урока',widget=CKEditorWidget())
    class Meta:
        model = Lesson
        fields = '__all__'



@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    admin customization
    """
    list_display = ('id','ch_lesson_name', )
    list_display_links = ('ch_lesson_name',)
    list_filter = ('topic',)
    search_fields = ('ch_lesson_name',)
    fieldsets = (
        ('Section 1',{
            'fields' : ('ch_lesson_name','topic'),
            'description': '%s' % 'Добавь урок и выбери курс к которому он относится',
        }),
        ('Section 2', {
            'fields': ('ch_lesson_plan', 'ch_lesson_text',),
            'description': '%s' % 'Напиши план урока и сам текст к нему',
        }),

    )
    form = LessonAdminForm      # this form allows us to edit it with CKE editor
    #inlines = [Video_Inline]

