from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from landing import views
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('restaurants/', RestaurantAPIView.as_view()),
    path('restaurants/sorted/', SortedView.as_view()),
    path('restaurants/luxury/', LuxuryView.as_view()),
    path('restaurants/with-item', FiltertedView.as_view())
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()