# nested duck arrays

There have been numerous discussions in 2021-2022 around how to deal with nested duck arrays[^1] [^2].

[^1]: https://github.com/pydata/duck-array-discussion
[^2]: https://discuss.scientific-python.org/t/creating-community-standards-for-meta-arrays-arrays-that-wrap-other-arrays/563

However, not a lot of progress has been made since then, in part because this is such a complex concept (even when limited to simple nesting) and possibly also because the scope might have been a bit too wide.

This library is a proof of concept to show that with fairly simple methods we can already achieve a lot. It is deliberately designed to deal only with _simple nesting_: arrays that wrap multiple other arrays would make a already complex concept even more tricky.

## examining the structure of the nesting

The library defines a new protocol, `__array_layers__`, that returns the type of each layer:

```python
import nested_duck_arrays.pint  # monkeypatches `pint.Quantity`
import nested_duck_arrays.dask  # monkeypatches `dask.array.Array`

import numpy as np
import sparse
import dask.array as da
import pint

ureg = pint.UnitRegistry()

arr = sparse.COO.from_numpy(np.arange(10))
q = ureg.Quantity(da.from_array(arr, chunks=(2,)), "m")
q.__array_layers__()
# (pint.Quantity, dask.array.core.Array, sparse._coo.core.COO)
```

This allows examining the structure of the duck array, and possibly special case certain libraries (in particular, `cupy` and `sparse`).
