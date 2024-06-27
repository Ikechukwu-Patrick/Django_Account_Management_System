from django.urls import path, include

from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('accounts', views.AccountViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('deposit', views.deposit),
    path('withdraw', views.withdraw),

]
