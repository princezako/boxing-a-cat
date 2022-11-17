import temp as m
import pytest

Example = m.Environment()
Example.WritePotential("")

def test_WritePotential_works():
    "Check that the code works as expected"
    string = "x"
    Example.WritePotential(string)
    assert Example.potential.any() == Example.x_array.any()

