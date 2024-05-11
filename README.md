DynaSift
========

DynaSift is a Python implementation of a hybrid algorithm that combines the Lorenz Attractor and Logistic Map. This repository provides a Python implementation of the DynaSift algorithm, along with examples and visualizations.

Getting Started
---------------

To use DynaSift, simply clone this repository and install the required dependencies using `pip`:
pip install -r requirements.txt

Then, run the `dynasift.py` script to generate the Lorenz Attractor and Logistic Map sequences.

Usage
-----

The `dynasift.py` script takes several command-line arguments:

* `--sigma`: The sigma parameter for the Lorenz Attractor (default: 10)
* `--rho`: The rho parameter for the Lorenz Attractor (default: 28)
* `--beta`: The beta parameter for the Lorenz Attractor (default: 8/3)
* `--r-logistic`: The r parameter for the Logistic Map (default: 3.9)
* `--initial-x`: The initial x value for the Logistic Map (default: 0.5)

Example usage:
python dynasift.py --sigma 10 --rho 28 --beta 8/3 --r-logistic 3.9 --initial-x 0.5

This will generate the Lorenz Attractor and Logistic Map sequences, and display the results using Matplotlib.

License
-------

DynaSift is licensed under the MIT License. See `LICENSE` for details.

Explanation
---------------

Explanation:
The code has been restructured into distinct functions:

1- `lorenz_system`: Defines the Lorenz system equations with customizable parameters.
2- `simulate_lorenz_attractor`: Solves the Lorenz equations over a specified time span.
3- `extract_samples_from_lorenz`: Samples points from the Lorenz attractor solution, focusing on a particular dimension.
4- `iterate_logistic_map`: Drives the logistic map iterations using an input sequence derived from the Lorenz attractor's path, with customizable `r_logistic` and initial `x0_logistic`.
5- `visualize_results`: Plots both the Lorenz attractor in 3D and the resulting logistic map sequence in a 2D plot for visual analysis.

These functions allow to have a more modular and understandable structure

. Each part of the process is separated, making it easier to modify or extend individual components without affecting the overall workflow.

The main execution flow then becomes straightforward:

* Define the parameters for the Lorenz system.
* Create the Lorenz system function using `lorenz_system`.
* Simulate the Lorenz attractor trajectory using `simulate_lorenz_attractor`.
* Sample points from the x-coordinate of the Lorenz attractor solution via `extract_samples_from_lorenz`.
* Generate the logistic map sequence using these sampled points with `iterate_logistic_map`.
* Finally, visualize the results using `visualize_results`.

By organizing the code in this manner, you can more easily experiment with different coupling mechanisms between the two systems, adjust parameters for both the Lorenz Attractor and the Logistic Map, and even introduce additional processing or analyses between the steps. This structure supports the ongoing refinement and expansion of "DynaSift," aligning with your goal of creating a novel, robust, and meaningful hybrid algorithm.

Contributing
------------

Contributions are welcome! If you'd like to contribute to DynaSift, please fork this repository and submit a pull request.

Acknowledgments
---------------

DynaSift was inspired by the work of [insert inspiration/reference].

Contact
-------

If you have any questions or issues, please don't hesitate to contact me.
