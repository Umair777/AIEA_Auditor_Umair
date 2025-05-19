import numpy as np

# Define the cost function to calculate Mean Squared Error
def compute_cost(x, y, theta0, theta1):
    m = len(y)  # Number of data points
    predictions = theta0 + theta1 * x  # Calculate predictions based on current theta values
    return np.sum((predictions - y) ** 2) / (2 * m)  # Calculate MSE

# Gradient function to calculate the derivatives of the cost function
def compute_gradients(x, y, theta0, theta1):
    m = len(x)
    predictions = theta0 + theta1 * x
    gradient_theta0 = np.sum(predictions - y) / m  # Derivative wrt theta0
    gradient_theta1 = np.sum((predictions - y) * x) / m  # Derivative wrt theta1
    return gradient_theta0, gradient_theta1

# Initialize parameters
theta0 = 1  # Initial guess for theta0
theta1 = 0.5  # Initial guess for theta1
alpha = 0.1  # Learning rate
tolerance = 1e-6  # Convergence criterion for stopping
max_iterations = 1000  # Maximum number of iterations
iterations = 0
cost_change = np.inf

# Data points
x = np.array([1, 2, 3])
y = np.array([3, 4, 5])

# Initial cost
current_cost = compute_cost(x, y, theta0, theta1)

# Gradient Descent Algorithm
while cost_change > tolerance and iterations < max_iterations:
    iterations += 1
    
    # Compute gradients
    gradient_theta0, gradient_theta1 = compute_gradients(x, y, theta0, theta1)
    
    # Update parameters
    theta0 -= alpha * gradient_theta0
    theta1 -= alpha * gradient_theta1
    
    # Calculate new cost
    new_cost = compute_cost(x, y, theta0, theta1)
    cost_change = abs(new_cost - current_cost)
    current_cost = new_cost
    
    # Output the iteration details
    print(f"Iteration {iterations}: Cost {new_cost:.6f}, Theta0 {theta0:.6f}, Theta1 {theta1:.6f}")

    # Check if cost change is less than the tolerance
    if cost_change < tolerance:
        print("Convergence reached.")
        break

# Final parameters and cost
print(f"Final parameters: Theta0 = {theta0:.6f}, Theta1 = {theta1:.6f}")
print(f"Final cost: {current_cost:.6f}")
