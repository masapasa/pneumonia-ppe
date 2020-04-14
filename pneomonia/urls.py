"""pneomonia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', v.home),
    path('team/', v.team),
    path('about/', v.about),
    path('badge_scan', v.badge_scan),
    path('', v.home),
    path('live_scan/', v.live_scan),
    path('ppe/', v.ppe),
    path('demo/', v.demo),
    path('uploadajax/', v.upload_data),
    path('demoajax/', v.demo_data),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)