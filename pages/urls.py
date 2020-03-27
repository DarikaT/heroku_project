from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home_url'), #когда подключаешь классы ОБЯЗАТЕЛЬНО используется as_view()
    path('about/', AboutPageView.as_view(), name = 'about_url')
]