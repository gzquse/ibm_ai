from qiskit.circuit.library import LinearFunction
from qiskit.synthesis.linear.linear_matrix_utils import random_invertible_binary_matrix

def get_random_linear_function(n_qubits, seeds):
    """
    Generate a random linear function circuit using the input parameters
    n_qubits, seed and through using the random_invertible_binary_matrix method
    """
    # Generate a random invertible binary matrix
    matrix = random_invertible_binary_matrix(n_qubits, seed=seeds)

    # Create a LinearFunction circuit from the matrix
    linear_function = LinearFunction(matrix)

    return linear_function

# This function takes in two parameters:
# 1. `n_qubits`: The number of qubits for the linear function.
# 2. `seeds`: The seed for the random number generator.

# The function returns a `LinearFunction` circuit that implements the random linear function based on the generated matrix.

