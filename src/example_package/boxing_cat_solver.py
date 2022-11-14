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
            c = PotentialModifier(self.x.array[0])
            if c != float(c) and c!=int(c):
                raise TypeError("Your choice should not be an array.") #to make sure that the program does not return an array
            elif "x" not in string:
                raise TypeError("Your choice should contain 'x'.")
            self.potential = PotentialModifier(self.x_array)

        else:
            raise TypeError("Your potential should be a string, dependent on x, such as x**2 or np.sin(x) etc.") #if the choice of potential is not a string
           
    def Make_gif(self):
        fig, ax = plt.subplots()
       
        ax.set_xlabel("x [arb units]")
        ax.set_ylabel("$|\Psi(x, t)|$", color="C0")
       
        ax_twin = ax.twinx()
        ax_twin.plot(self.x_array, self.potential, color="C1")
        ax_twin.set_ylabel("V(x) [arb units]", color="C1")
        if np.min(self.potential) != np.max(self.potential):
            ax_twin.set_ylim(np.min(self.potential),np.max(self.potential))
       
        line, = ax.plot([], [], color="C0", lw=2)
        ax.grid()
        xdata, ydata = [], []
 
        def run(psi):
            line.set_data(self.x_array, np.abs(psi)**2)
            return line,
       
        ax.set_xlim(self.x_array[0], self.x_array[-1])
        ax.set_ylim(0, 1)
       
        ani = animation.FuncAnimation(fig, run, self.psi_list, interval = 20, blit = True)
        writergif = animation.PillowWriter()
        ani.save("new_gif.gif", writer=writergif)
   
    def solve_schrodinger(self, N = 100):
        self.psi = np.exp(-(self.x_array+2)**2)
       
        #Calculate derivatives
        dt = self.t_array[1] - self.t_array[0]
        dx = self.x_array[1] - self.x_array[0]
       
        #Turn potential into a diagonal matrix
        potential_matrix = diags(self.potential)
       
        #Calculate Hamiltonian matrix, apply boundary conditions
        H = -0.5 * FinDiff(0,dx,2).matrix(self.x_array.shape) + potential_matrix
       
        H[0,:] = H[-1,:] = 0
        H[0,0] = H[-1,-1] = 1
        #Calculate U
        I_plus = eye(self.Nx) + 1j * dt / 2. * H
        I_minus = eye(self.Nx) - 1j * dt / 2. * H
        U = inv(I_minus).dot(I_plus)
       
        #Iterate over time and append psi value to a list
        self.psi_list = []
        for t in self.t_array:
            self.psi = U.dot(self.psi)
            self.psi[0] = self.psi[-1] = 0
            self.psi_list.append(np.abs(self.psi))        
               
# This is an example of how the code is used        
Env1 = Environment()
print(Env1.potential)
Env1.zero_potential()
Env1.WritePotential("x**2")
print(Env1.potential)