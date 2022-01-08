from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms

from .models import Lesson_Video, Lesson


# admin.site.register(Lesson)
# admin.site.register(Lesson_Video)

# @admin.register(Lesson)

@admin.register(Lesson_Video)
class LessonVideoAdmin(admin.ModelAdmin):
    """
    admin customization
    """
    list_display = ('id','ch_video_name', 'ch_video_link',)
    list_display_links = ('ch_video_name', 'ch_video_link')
    #list_filter = ('id',)
    search_fields = ('ch_video_name',)






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
    list_display = ('id','ch_lesson_name', 'i_course_id')
    list_display_links = ('ch_lesson_name','i_course_id')
    list_filter = ('i_course_id',)
    search_fields = ('ch_lesson_name',)
    fieldsets = (
        ('Section 1',{
            'fields' : ('i_course_id', 'ch_lesson_name',),
            'description': '%s' % 'Добавь урок и выбери курс к которому он относится',
        }),
        ('Section 2', {
            'fields': ('ch_lesson_plan', 'ch_lesson_text',),
            'description': '%s' % 'Напиши план урока и сам текст к нему',
        }),
        ('Section 3', {
            'fields': ('i_video',),
            'description': '%s' % 'А теперь прикрепи сюда видео, солнышко',
        })

        ,
    )
    form = LessonAdminForm      # this form allows us to edit it with CKE editor
    #inlines = [Video_Inline]

