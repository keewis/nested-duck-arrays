def layers(x):
    """extract the layers of a duck array

    Parameters
    ----------
    x : array-like
        The duck array. If it has the ``__array_layers__`` protocol, it will be
        called. Otherwise the type of the duck array will be returned as a 1-tuple.

    Returns
    -------
    layers : tuple of type
        The classes of the layers, with the outermost layer first.
    """

    try:
        return x.__array_layers__()
    except AttributeError:
        return (type(x),)


def first_layer(x):
    """extract the innermost layer of the duck array

    See also
    --------
    layers
    """
    return layers(x)[-1]
