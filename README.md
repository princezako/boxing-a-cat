# Template repository for PH3010 Advanced Python

This package provides solutions to Schrödinger's equation for a particle in a 1D infinite potential square well. The user should use the code by setting values for the minimum and maximum x-values for the position of the particle with variable names x_min and x_max. They should also set values for the minimum and maximum values of time with variables t_min and t_max as well as the total number of position and time values with variable names Nx and Nt. Also, the user should define the equation that is being used with the PotentialModifier(x) function, making sure that for each input of the equation there is only a singular value output. The package then calculates the derivatives of the position and time and converts the x-values and potential into a diagonal matrix. From this, the hamiltonian matrix can be created which gives the energy eigenvalues of the equation allowing for an iterative equation for the potential to be created. This is then used to calculate the energy states of the particle over time which can then be represented as a moving visualisation.

This is a template repository demonstrating how to package a python project. The directory is structured as follows:
```

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
│       ├── example.py
│       └── boxing_cat_solver.py
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
