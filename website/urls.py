from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
