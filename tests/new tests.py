import boxing_cat_solver as m
import pytest

 

Example = m.Environment()
Example.Write_potential("np.sin(x)")

 

def test_WritePotential_works():
    "Check that the code works as expected"
    string = "x"
    Example.Write_potential(string)
    assert Example.potential.any() == Example.x_array.any()



def test_WritePotential_fails_1():
    
    string = "float"
    Example.Write_potential(string)
    with pytest.raises(TypeError):
         Example.Write_potential(string)
        
def test_WritePotential_fails_2():
    
    string = 3
    Example.Write_potential(string)
    with pytest.raises(TypeError):
         Example.Write_potential(string)
        
        
