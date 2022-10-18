"""workshop_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from home.views import home_page

from users.views import user_view
from users.views import edit_user
from users.views import delete_user

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home_page),

    path("users/", user_view),

    path("users/edituser/<str:email>/<str:user>/", edit_user),
    path("users/deleteuser/<str:email>/<str:user>/", delete_user),
]

urlpatterns += staticfiles_urlpatterns()
