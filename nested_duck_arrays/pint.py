import pint

from nested_duck_arrays.common import create_protocol

pint.Quantity.__duck_arrays__ = create_protocol("magnitude")
