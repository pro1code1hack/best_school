from django.contrib import admin

from school_users.models import UserProfile
from .models import CourseInfo, SubscriptionType, UserCourses , UserRanking


# admin.site.register(CourseInfo)
#admin.register(SubscriptionType)
#admin.site.register(UserCourses)
admin.site.register(UserRanking)


class UserSubscriptionsInline(admin.TabularInline):
    """
    Shows which users bought the subscription
    """
    model = UserCourses


# class UserCoursesInline(admin.TabularInline):
#     model = UserProfile

@admin.register(UserCourses)
class UserCoursesAdmin(admin.ModelAdmin):
    list_display = ('i_subscription_type', 'i_course_id', 'i_user_id')


    # inlines = [UserCoursesInline]


@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'ch_name', 'fl_price')
    list_display_links = ('ch_name',)
    list_filter = ('ch_name','fl_price')
    search_fields = ('ch_name',)

@admin.register(CourseInfo)
class CourseInfoAdmin(admin.ModelAdmin):
    """
    admin customization
    """
    list_display = ('id','ch_name')
    list_display_links = ('ch_name',)
    list_filter = ('ch_name',)
    search_fields = ('ch_name',)





# Register your models here.
