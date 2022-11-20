# Template repository for PH3010 Advanced Python

This is a repository demonstrating how to use the boxing-a-cat package for python.

The package takes input values for the Schrödinger equation and provides solutions in the form of an array of values which can then be plotted onto a graph to visualise how the potential and the value wavefunction probability interact. To start the package you have to define an enviroment in which the equation can be solved. One should do this with the function Env1 = boxing_cat_solver.Enviroment(Arguments) where Env1 can be replaced with a generic name for the current trial of the package. There are a number of variables you can change such as the potential function which can be edited with the function Env1.Write_Potential("f(x)") in which f(x) is a function of x that must have a single solution for a given input otherwise the package will fail. Alternatively, there is the option to draw the potential with the function Env1.Draw_Potential() which brings up a box in a window that allows you to draw the potential function of the wavefunction by free hand. You can also reset the potential to its original value with the function Env1.Zero_Potential. When you are happy with the conditions set, you then use Env1.Solve-Schrodinger(Args) to start the computation of the solutions. This outputs an array of values that are solutions to your customizable wavefunction which can also be visualised on a graph using the function Env1.Make_gif() which provides a moving visualisation of the solutions compared to the potential function. 

To import package:
from Group_E_Package import boxing_cat_solver

This package is uploaded on TestPYPI. To install the package visit:
https://test.pypi.org/project/boxing-cat-solver/0.0.1/


template_project_PH3010_advanced_python/
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
├── setup.cfg
├── .github/
│   └── workflows/
│              └── python_test.yml
├── docs/
│   └── ../
│   └── workflows/
├── src/
│   └── example_package/
│       ├── __init__.py
│       ├── command_line_interface.py
│       ├── boxing_cat_solver.py    <-------- Package
│       └── example.py
└── tests/
        └── test_example.py
```

Let's look at each element individually

* `.gitignore` contains files that should be ignored by git
* `LICENSE` the project license telling users who install your package the terms under which they can use your package
* `README.md` A [markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) document telling users about the project
* `pyproject.toml` tells build tools (like pip and build) what is required to build your project.
* `requirements.txt` contains the requirements for the project, you can install these with `pip install -r requirements.txt`
* `docs/` contains the documentation - we won't discuss this further here.
* `.github/workflows/python_test.yml` contains a [YAML](https://yaml.org/) file which determined how github Action are run
* `src/` contains the python package itself
* `tests/` contains the tests of the python package
