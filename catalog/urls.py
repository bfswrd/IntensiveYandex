from django.urls import path, re_path

import catalog.views

app_name = "catalog"

urlpatterns = [
    path("", catalog.views.item_list, name="item_list"),
    # Start with 1, 0 is incorrect
    re_path(r"^(?P<pk>[1-9]\d*)/$", catalog.views.item_detail,
            name="item_detail"),
]
