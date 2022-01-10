from django.contrib import admin
from .models import  UserProfile
    #UserMetrics, MetricsType


# @admin.register(UserAuth)
# class UserAuthAdmin(admin.ModelAdmin):
#     """
#         admin customization
#     """
#     list_display = ('id', 'ch_username', 'b_is_active')
#     list_display_links = ('ch_username',)
#     list_filter = ('b_is_active',)
#     search_fields = ('ch_username','id')


admin.site.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'ch_name', 'ch_surname','dt_register_date', 'dt_total_time_on_the_website')
#     list_display_links = ('ch_name',)
#     list_filter = ('dt_register_date','dt_total_time_on_the_website')
#     search_fields = ('ch_name',)

# @admin.register(UserMetrics)
# class UserMetricsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'i_user_id', 'i_metrics_type', 'i_metrics_value')
#     list_display_links = ('i_user_id',)
#     list_filter = ('i_metrics_type', 'i_metrics_value')
#
#
# @admin.register(MetricsType)
# class MetricsTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'i_metrics_type', 'ch_metrics_name',)
#     list_display_links = ('i_metrics_type', 'ch_metrics_name')
#     list_filter = ('i_metrics_type',)
#
#     pass

# admin.site.register(UserAuth)
# admin.site.register(UserProfile)
# admin.site.register(UserMetrics)
# admin.site.register(MetricsType)

# Register your models here.