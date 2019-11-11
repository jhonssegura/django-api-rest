# -*- coding: utf-8 -*-	
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api_rest import views
from rest_framework.authtoken import views as view_token
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Pastebin API')

router = routers.DefaultRouter()
router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'profesores', views.ProfesorViewSet)
router.register(r'materias', views.MateriaViewSet)

urlpatterns = [
    # URLs Aplication REST
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', view_token.obtain_auth_token),
    # URL Swagger
    url(r'^swagger/', schema_view),
    #URL Cantidad Balanzas por Sucursal
    #url(r'^Estudiantes/', views.EstudianteView.as_view()),
    #url(r'^Profesores/', views.ProfesorView.as_view()),
    #url(r'^Materias/', views.MateriaView.as_view()),
    # URL Administrator
    url(r'^admin/', admin.site.urls),
    # URL Documentacion
    url(r'^docs/', include_docs_urls(title='API Balanzas')),
]
