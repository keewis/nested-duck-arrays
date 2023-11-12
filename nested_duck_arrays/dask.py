import dask.array as da

from nested_duck_arrays.common import create_protocol

da.Array.__duck_arrays__ = create_protocol("_meta")
