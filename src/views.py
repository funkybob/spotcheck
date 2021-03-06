from paws import http_handler
from paws.response import response

from stencil import Context

from models import PageStorage, TemplateStorage
import tags  # NOQA


def slots_for_template(tmpl):
    '''
    Get a set of slot names for this template.
    '''
    return {
        tag.name
        for tag in tmpl.nodes_by_type(tags.SlotNode)
    }


@http_handler
def default(request, path):
    try:
        page = PageStorage.get(key=path or '/')
    except LookupError:
        return response(status=404)

    try:
        tmpl = TemplateStorage.get(key=page.template)
    except LookupError:
        try:
            tmpl = TemplateStorage.get(key='default.html')
        except LookupError:
            return response('No template defined', status=500)

    # Load context
    ctx = Context({'page': page})

    return response(
        tmpl.render(ctx),
        headers={'Content-Type': 'text/html'}
    )
