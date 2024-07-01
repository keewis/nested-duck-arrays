def create_protocol(attribute):
    def __array_layers__(self):
        wrapped = getattr(self, attribute)

        try:
            wrapped_types = tuple(wrapped.__array_layers__())
        except AttributeError:
            wrapped_types = (type(wrapped),)

        return (type(self),) + wrapped_types

    return __array_layers__
