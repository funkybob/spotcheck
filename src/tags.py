import stencil


class SlotNode(stencil.BlockNode):
    name = 'slot'

    def __init__(self, name):
        self.name = name

    @classmethod
    def parse(cls, content, parser):
        name = content.strip().split()[0]
        return cls(name)

    def render(self, context, output):
        for widget in context['slots'].get(self.name, []):
            widget.render(context, output)
