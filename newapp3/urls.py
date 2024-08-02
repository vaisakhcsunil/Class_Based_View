from newapp3.views import myview
from .import views
from django.urls import path
urlpatterns=[
    path('myview/',myview.as_view()),
]