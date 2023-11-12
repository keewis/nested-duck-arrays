def create_protocol(attribute):
    def __duck_array__(self):
        wrapped = getattr(self, attribute)

        try:
            wrapped_types = tuple(wrapped.__duck_arrays__())
        except AttributeError:
            wrapped_types = (type(wrapped),)

        return (type(self),) + wrapped_types

    return __duck_array__
