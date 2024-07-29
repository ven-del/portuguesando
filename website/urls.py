from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static
from .views import login, home, sobre, aulas, downloads

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('login/', login, name='login'),
    path('aulas/', aulas, name='aulas'),
    path('downloads/', downloads, name='downloads'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
