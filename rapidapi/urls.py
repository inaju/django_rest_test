from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='rest_framswork')
]
