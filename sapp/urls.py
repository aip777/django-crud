from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home),
    path('create', StudentCreateView.as_view(),name='create'),
    path('update/<int:pk>', StudentUpdateView.as_view(),name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),

]