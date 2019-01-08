from celery import shared_task


@shared_task
def create_pdf_task(pdfrender_id):
    from .models import PDFRender

    try:
        pdfrender = PDFRender.objects.get(id=pdfrender_id)
    except PDFRender.DoesNotExist:
        return

    pdfrender.create_pdf()
