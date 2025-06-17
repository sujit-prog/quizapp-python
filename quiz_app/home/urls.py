from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('quiz/', views.quiz_page, name='quiz_page'),
    path('api/get-quiz/', views.get_quiz_api, name='get_quiz_api'),
    path('result/', views.result, name='result'),  # NEW route for result page
]
