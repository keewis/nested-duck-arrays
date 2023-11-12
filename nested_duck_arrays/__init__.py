from importlib.metadata import version

try:
    __version__ = version("nested_duck_arrays")
except Exception:
    __version__ = "9999"
