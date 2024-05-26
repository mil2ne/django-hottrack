from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hottrack/", include("hottrack.urls")),
    path(route="", view=lambda request: redirect("/hottrack/")),
]
