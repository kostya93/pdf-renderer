class PDFRenderStatus(object):
    PENDING = 1
    SUCCESS = 2
    FAILED = 3

    CHOICES = (
        (PENDING, 'pending'),
        (SUCCESS, 'success'),
        (FAILED, 'failed'),
    )

    NAMES = dict(CHOICES)


WKHTMLTOPDF_COMMAND = 'xvfb-run --server-args="-screen 0, 1024x768x24" wkhtmltopdf -q {url} -'
