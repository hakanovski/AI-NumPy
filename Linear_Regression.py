import numpy as np
import matplotlib.pyplot as plt

# Generating a synthetic dataset
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Function to compute the cost
def compute_cost(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    cost = (1/2*m) * np.sum(np.square(predictions - y))
    return cost

# Function for gradient descent
def gradient_descent(X, y, theta, learning_rate=0.01, iterations=1000):
    m = len(y)
    cost_history = np.zeros(iterations)
    theta_history = np.zeros((iterations, 2))
    
    for i in range(iterations):
        prediction = np.dot(X, theta)
        theta = theta - (1/m) * learning_rate * (X.T.dot((prediction - y)))
        cost_history[i] = compute_cost(X, y, theta)
        theta_history[i,:] = theta.T
    
    return theta, cost_history, theta_history

# Adding a bias term to X
X_b = np.c_[np.ones((len(X), 1)), X]

# Initial theta (weights)
theta = np.random.randn(2,1)

# Parameters for the gradient descent
learning_rate = 0.01
iterations = 1000

# Performing gradient descent
theta_best, cost_history, theta_history = gradient_descent(X_b, y, theta, learning_rate, iterations)

# Plotting the cost history
plt.plot(range(iterations), cost_history)
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Cost Function Over Iterations")
plt.show()

# The final model parameters
theta_best
