import dask.array as da

from nested_duck_arrays.common import create_protocol

da.Array.__array_layers__ = create_protocol("_meta")
