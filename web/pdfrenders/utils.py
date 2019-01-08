import resource
import subprocess

from django.conf import settings

from .constants import WKHTMLTOPDF_COMMAND


class PDFCreatingError(Exception):
    pass


def create_pdf_command(url='-', html=None):
    def set_limits():
        time = settings.PDFRENDERS_CREATE_PDF_COMMAND_TIME_LIMIT_SECONDS
        resource.setrlimit(resource.RLIMIT_CPU, (time, time))

    subproc = subprocess.Popen(WKHTMLTOPDF_COMMAND.format(url=url),
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               preexec_fn=set_limits,
                               shell=True)

    try:
        outputs, errors = subproc.communicate(
            input=html,
            timeout=settings.PDFRENDERS_CREATE_PDF_COMMAND_TIMEOUT_LIMIT_SECONDS
        )
    except subprocess.TimeoutExpired:
        subproc.kill()
        outputs, errors = subproc.communicate()

    if subproc.returncode:
        raise PDFCreatingError(f'Failed to create pdf; '
                               f'return code: {subproc.returncode}; '
                               f'outputs: {outputs}; '
                               f'errors: {errors}')

    return outputs
