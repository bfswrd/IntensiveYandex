from django.urls import path

from homepage.views import Home

app_name = "homepage"

urlpatterns = [
    path("", Home.as_view(), name="home"),
]
