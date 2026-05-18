import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def backward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, y_true: float) -> Tuple[NDArray[np.float64], float]:
        # x: 1D input array
        # w: 1D weight array
        # b: scalar bias
        # y_true: true target value
        #
        # Forward: z = dot(x, w) + b, y_hat = sigmoid(z)
        # Loss: L = 0.5 * (y_hat - y_true)^2
        # Return: (dL_dw rounded to 5 decimals, dL_db rounded to 5 decimals)
        z = np.dot(x, w) + b
        y_hat = 1.0 / (1.0 + np.exp(-z))

        # chain rule 1
        error = y_hat - y_true
        # chain rule 2
        sigmoid_derivative = y_hat * (1 - y_hat)
        # multiply together as per chain rule
        delta = error * sigmoid_derivative
        # chain rule 3a (* x)
        dL_dw = np.round(x * delta, 5)
        # chain rule 3b (* 1, since dz/db = 1)
        dL_db = round(float(delta), 5)

        return (dL_dw, dL_db) # now know how the loss has been impacted by our weight and bias choices.


