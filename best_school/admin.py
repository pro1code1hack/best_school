# from django.contrib import admin
# import django.apps
#
# models = django.apps.apps.get_models()
# print(models)
#
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
#
# admin.site.unregister(django.contrib.sessions.models.Session)