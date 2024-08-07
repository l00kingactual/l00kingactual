import numpy as np

def finite_difference_gradient(f, w, epsilon=1e-5):
    grad = np.zeros_like(w)
    for i in range(len(w)):
        w_perturbed = w.copy()
        w_perturbed[i] += epsilon
        grad[i] = (f(w_perturbed) - f(w)) / epsilon
    return grad

# Example loss function (sum of squares)
def loss_function(w):
    return np.sum(w ** 2)

# Initial weights
w = np.array([1.0, -2.0, 3.0])
gradient = finite_difference_gradient(loss_function, w)
print("Finite Difference Gradient:", gradient)
