from django.contrib import admin

from .models import PDFRender


class PDFRenderAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_date', 'update_date', 'status', 'url',
                    'html_file', 'pdf_file']
    list_filter = ['status']
    search_fields = ['url']


admin.site.register(PDFRender, PDFRenderAdmin)
