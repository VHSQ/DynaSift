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

Contributing
------------

Contributions are welcome! If you'd like to contribute to DynaSift, please fork this repository and submit a pull request.

Acknowledgments
---------------

DynaSift was inspired by the work of [insert inspiration/reference].

Contact
-------

If you have any questions or issues, please don't hesitate to contact me.
