from rest_framework import serializers

from .constants import PDFRenderStatus
from .models import PDFRender


class PDFRenderSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = PDFRender
        fields = ['id', 'url', 'status', 'html_file', 'pdf_file']
        read_only_fields = ['status', 'pdf_file']

    def get_status(self, obj):
        return PDFRenderStatus.NAMES[obj.status]

    def validate(self, attrs):
        if 'url' in attrs and 'html_file' in attrs:
            raise serializers.ValidationError('Specify only one of fields [url, html_file]')

        return attrs
