import logging
import os
import uuid

from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .constants import PDFRenderStatus
from .tasks import create_pdf_task
from .utils import create_pdf_command, PDFCreatingError


logger = logging.getLogger(__name__)


def html_upload_to(instance, filename):
    return os.path.join('html', f'{instance.id}.html')


def pdf_upload_to(instance, filename):
    return os.path.join('pdf', f'{instance.id}.pdf')


class PDFRender(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    create_date = models.DateTimeField(db_index=True, auto_now_add=True)
    update_date = models.DateTimeField(db_index=True, auto_now=True)

    status = models.SmallIntegerField(db_index=True, choices=PDFRenderStatus.CHOICES,
                                      default=PDFRenderStatus.PENDING)

    url = models.URLField(blank=True, null=True)
    html_file = models.FileField(blank=True, null=True, upload_to=html_upload_to)
    pdf_file = models.FileField(blank=True, null=True, upload_to=pdf_upload_to)

    objects = models.Manager()

    def create_pdf(self):
        def fail_render(msg):
            logger.error(msg)
            self.status = PDFRenderStatus.FAILED
            self.save(update_fields=['status'])

        if not self.url and not self.html_file:
            fail_render('Can not create pdf without url and html_file')
            return

        try:
            if self.url:
                pdf = create_pdf_command(url=self.url)
            else:
                pdf = create_pdf_command(html=self.html_file.read())
        except PDFCreatingError as error:
            fail_render(str(error))
            return

        self.pdf_file.save('pdf', ContentFile(pdf), save=False)
        self.status = PDFRenderStatus.SUCCESS
        self.save(update_fields=['status', 'pdf_file'])

    def create_pdf_async(self):
        create_pdf_task.delay(self.id)

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=PDFRender)
def pdf_render_created(sender, instance, created, **kwargs):
    if created:
        instance.create_pdf_async()
