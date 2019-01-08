from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import PDFRender
from .serializers import PDFRenderSerializer


class PDFRenderViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    class Meta:
        model = PDFRender

    queryset = PDFRender.objects.all()
    serializer_class = PDFRenderSerializer
