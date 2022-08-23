from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_doc, name="register"),
    path('registerpat/', views.register_pat, name='registerpat'),
    path('login/', views.login, name='login')
]
