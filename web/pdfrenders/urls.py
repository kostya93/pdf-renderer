from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'pdfrenders', views.PDFRenderViewSet)

urlpatterns = router.urls
