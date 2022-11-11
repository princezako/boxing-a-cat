### Required imports ###
import numpy as np
import matplotlib.pyplot as plt
from findiff import FinDiff
from scipy.sparse.linalg import inv
from scipy.sparse import eye, diags
import matplotlib.animation as animation

plt.rcParams["axes.labelsize"] = 16

### This section will deal with defining the potential ###
class Environment():
    def __init__(self,x_min = -5,x_max = 5,t_min = 0,t_max = 20, Nx = 500, Nt = 250):
        # The x_min = -5 and so on ensures that the class always starts with a preset which can be modified by the user
        # in other words there are no problems if the user forgets to define one of the above
        
        # This sets up the x_array
        self.x_min = x_min 
        self.x_max = x_max
        self.Nx = Nx
        self.x_array = np.linspace(x_min,x_max,Nx)
        # This sets up the t_array that is required by the code
        self.t_min = t_min
        self.t_max = t_max
        self.Nt = Nt
        self.t_array = np.linspace(t_min,t_max,Nt)
        # This ensures a potential is always generated initially so the user doesn't need to do anything fancy if they just
        # want a simple potential well
        self.potential = np.array(len(self.x_array)*[0])
    
    def zero_potential(self):
        # This is a simple function that sets everything to zero
        self.potential = np.array(len(self.x_array)*[0])
    
    def WritePotential(self,string):
        if string == str(string): # Error team needs to write a response if this isn't true
            # Error and annotation team also need to make sure that it's clear people only need to input functions like
            # "x**2" and "np.sin(x)". x must be included and it is run as code so it will give a lot of errors if misused.
            # Also since this is code, any imported module that returns a single number can be used, maybe a test could be
            # to use the PotentialModifier function immediately after it is defined and ensure it results in one number per
            # number inputted
            code = """def PotentialModifier(x):
    return """ + string
            exec(code, globals())
            self.potential = PotentialModifier(self.x_array)
                
# This is an example of how the code is used        
Env1 = Environment()
print(Env1.potential)
Env1.zero_potential()
Env1.WritePotential("x**2")
print(Env1.potential)
