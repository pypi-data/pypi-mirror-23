import logging
from io import BytesIO

from django.core.urlresolvers import NoReverseMatch
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.translation import ugettext as _

from page_exporter.config import conf
from page_exporter.utils import (page_capture, CaptureError, UnsupportedImageFormat,
                    image_mimetype, parse_url)

logger = logging.getLogger(__name__)


def capture(request):
    # Merge both QueryDict into dict
    parameters = dict([(k, v) for k, v in request.GET.items()])
    parameters.update(dict([(k, v) for k, v in request.POST.items()]))

    url = parameters.get('url')
    if not url:
        return HttpResponseBadRequest(_('Missing url parameter'))
    try:
        url = parse_url(request, url)
    except NoReverseMatch:
        error_msg = _("URL '%s' invalid (could not reverse)") % url
        return HttpResponseBadRequest(error_msg)

    method = parameters.get('method', request.method)
    selector = parameters.get('selector')
    data = parameters.get('data')
    waitfor = parameters.get('waitfor')
    wait = parameters.get('wait', conf.WAIT)
    render = parameters.get('render', 'png')
    size = parameters.get('size')
    crop = parameters.get('crop')
    cookie_name = parameters.get('cookie_name')
    cookie_value = parameters.get('cookie_value')
    cookie_domain = parameters.get('cookie_domain')
    page_status = parameters.get('page_status')

    try:
        width = int(parameters.get('width', ''))
    except ValueError:
        width = None
    try:
        height = int(parameters.get('height', ''))
    except ValueError:
        height = None

    stream = BytesIO()
    try:
        page_capture(stream, url, method=method.lower(), width=width,
                     height=height, selector=selector, data=data,
                     size=size, waitfor=waitfor, crop=crop, render=render,
                     wait=wait, cookie_name=cookie_name, cookie_value=cookie_value,
                     cookie_domain=cookie_domain, page_status=page_status)
    except CaptureError as e:
        return HttpResponseBadRequest(e)
    except ImportError:
        error_msg = _('Resize not supported (PIL not available)')
        return HttpResponseBadRequest(error_msg)
    except UnsupportedImageFormat:
        error_msg = _('Unsupported image format: %s' % render)
        return HttpResponseBadRequest(error_msg)

    response = HttpResponse(content_type=image_mimetype(render))
    response.write(stream.getvalue())

    return response
