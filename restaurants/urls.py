from django.urls import path
from django.conf.urls import include, url

from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash = False)
router.register (r'api/establecimientos', views.EstablecimientoViewSet)
router.register (r'api/todos-codigos', views.ConductorCuponesViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('', views.index, name='index'),
    url(r'^api/codigo-conductor/(?P<user_id>[0-9]+)/$', views.UserProductsList.as_view()),
    
]