

class buffered_property(object):
    def __init__(self, getter):
        self.func = getter
        self.__name__ = getter.__name__

    def __get__(self, instance, klass):
        if instance is None:
            return self

        val = instance.__dict__[self.func.__name__] = self.func(self)
        return val
