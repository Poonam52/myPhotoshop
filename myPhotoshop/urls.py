"""myPhotoshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
#from rest_framework import routers
from rest_framework import viewsets, routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
# from django.contrib import admin
# from webapp.views import viewPhotoshopAPP
from webapp import views

router = routers.DefaultRouter()
router.register(r'ImageProcess', views.ImageProcessViewSet)
from webapp.forms import ImageForm
from webapp.models import imageProcess

schema_view = get_swagger_view(title='Photoshop API')

from webapp.views import ProcessImageCreateAPIView, ProcessImage,GetManipulated_Image

urlpatterns = [
    path('testdev', ProcessImage.as_view(), name='index'),
    #Swagger Doc API
    re_path('^$', schema_view),
    re_path(r'^', include(router.urls)),
    #path('photoviewset', include(router.urls)),
    path('UploadImage', ProcessImageCreateAPIView.as_view(), name='ProcessImageCreateAPIView'),
    path('GetManipulated_Image',GetManipulated_Image),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
        title="Photoshop Swagger Schema API",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


