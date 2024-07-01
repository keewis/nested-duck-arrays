from importlib.metadata import version

from nested_duck_arrays.api import first_layer, layers  # noqa: F401

try:
    __version__ = version("nested_duck_arrays")
except Exception:
    __version__ = "9999"
