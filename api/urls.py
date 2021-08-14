from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register("products",views.ProductModelViewSet,basename="products")


urlpatterns = [
    path("",views.myHome),
    path("apii/",views.myApi),
   path("api/",include(router.urls)),
]
