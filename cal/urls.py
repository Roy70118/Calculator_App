from django.urls import path
from .views import cal_view
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
urlpatterns = [
    path('', cal_view, name='cal'),
    path('favicon.ico', lambda request: HttpResponse(
        '', content_type='image/x-icon')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
