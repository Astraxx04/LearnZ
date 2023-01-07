"""LearnZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from courses.views import *
from authentication.views import *
from features.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('',include('courses.urls')),
    path('',include('UploadFiles.urls')),
    path('index/', index, name='index'),
    path('courses/', course_page, name='course_page'),
    path('', include('features.urls')),
    # path('features/', studentFeatures, name='feature_page_student'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

