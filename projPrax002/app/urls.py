from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='home'),
    path('alta_elementos', views.alta_elementos, name='alta_elementos'),
    path('editar_elementos/<id>', views.editar_elementos, name='editar_elementos'),
    path('editar_participantes/<id>', views.editar_participantes, name='editar_participantes'),
    path('consulta_elementos', views.consulta_elementos, name='consulta_elementos'),
    path('alta_participantes', views.alta_participantes, name='alta_participantes'),
    path('consulta_participantes', views.consulta_participantes, name='consulta_participantes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
