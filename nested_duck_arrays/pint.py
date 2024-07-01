import pint

from nested_duck_arrays.common import create_protocol

pint.Quantity.__array_layers__ = create_protocol("magnitude")
