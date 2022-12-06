from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView,
                                       PasswordResetConfirmView,
                                       PasswordResetView)
from django.urls import path, re_path, reverse_lazy
from django.views.generic import RedirectView

from homepage.views import Home
from users.views import Profile, signup, user_detail, user_list

app_name = "users"

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("profile/", Profile.as_view(), name="profile"),
    path("user_list/", user_list, name="user_list"),
    re_path(r"^user_detail/(?P<pk>[1-9]\d*)/$", user_detail,
            name="user_detail"),

    path("login/",
         LoginView.as_view(template_name="users/login.html",
                           extra_context={"name": "Вход"}),
         name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("password_change/",
         PasswordChangeView.as_view(
             template_name="users/login.html",
             success_url=reverse_lazy("users:password_change_done"),
             extra_context={"name": "Смена пароля",
                            "button": "Подтвердить"}
         ), name="password_change"),

    path("password_change/done/", Home.as_view(
        extra_context={"alert": "Пароль успешно изменен"}
    ), name="password_change_done"),

    path("password_reset/", PasswordResetView.as_view(
        email_template_name="users/password_reset_confirm.html",
        subject_template_name="users/password_reset_subject.txt",
        template_name="users/login.html",
        success_url=reverse_lazy("users:password_reset_done"),
        extra_context={"name": "Сброс пароля",
                       "button": "Подтвердить"}
    ), name="password_reset"),

    path("password_reset/done/", Home.as_view(
        extra_context={
            "alert": "Вы успешно сбросили пароль, "
                     "скоро вам на почту придет уведомление"
        }
    ), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(
        template_name="users/login.html",
        success_url=reverse_lazy("users:password_reset_complete"),
        extra_context={
            "alert": "Введите новый пароль",
            "name": "Восстановление пароля",
            "button": "Подтвердить",
        }
    ),
        name="password_reset_confirm"),
    path("reset/done/", Home.as_view(
        extra_context={
            "alert": "Пароль сброшен"
        }
    ),
        name="password_reset_complete"),
    path("", RedirectView.as_view(url=reverse_lazy("homepage:home")))
]
