from mannequin import Model
from mannequin import attrs
from mannequin.stores.dynamodb import DynamoStore

import stencil

from conf import conf
from utils import buffered_property


class Template(Model):
    name = attrs.StringAttr()
    content = attrs.StringAttr()

    @buffered_property
    def template(self):
        return stencil.Template(self.content)

    def render(self, context):
        return self.template.render(context)


class Page(Model):
    path = attrs.StringAttr()  # PathAttr?
    template = attrs.StringAttr()


TemplateStorage = DynamoStore(Template, hash_key='name', table=conf.TEMPLATE_TABLE)
PageStorage = DynamoStore(Page, hash_key='path', table=conf.PAGE_TABLE)
