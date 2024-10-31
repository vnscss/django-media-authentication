from django.urls import path , re_path
from . import views

urlpatterns = [
    re_path(r'^media/(?P<path>.*)', SUA-VIEWS.media_access, name='media')
]
