"""
URL configuration for tunetalk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from album_review import views

urlpatterns = [
    path('', include('album_review.urls'), name="album_review-urls"),
     path('rate/<int:album_id>/<int:rating>/', views.rate),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
]
