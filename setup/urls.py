from django.contrib import admin
from django.urls import path

from users.views import users_list


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", users_list),
]
