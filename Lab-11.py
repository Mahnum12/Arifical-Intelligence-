# Function to calculate the mean of an array
def calculate_mean(values):
    return sum(values) / len(values)

# Function to calculate the slope (theta_1)
def calculate_slope(X, Y, mean_X, mean_Y):
    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X)))
    denominator = sum((X[i] - mean_X) ** 2 for i in range(len(X)))
    return numerator / denominator

# Function to calculate the intercept (theta_0)
def calculate_intercept(mean_X, mean_Y, slope):
    return mean_Y - slope * mean_X

# Function to make predictions
def predict(X, theta_0, theta_1):
    return [theta_0 + theta_1 * x for x in X]

# Function to calculate Mean Squared Error (MSE)
def calculate_mse(Y, Y_pred):
    errors = [(Y[i] - Y_pred[i]) ** 2 for i in range(len(Y))]
    return sum(errors) / len(Y)

# Function to perform gradient descent
def gradient_descent(X, Y, theta_0, theta_1, learning_rate, iterations):
    n = len(X)
    for _ in range(iterations):
    
        Y_pred = predict(X, theta_0, theta_1)
        
        d_theta_0 = -2 / n * sum(Y[i] - Y_pred[i] for i in range(n))
        d_theta_1 = -2 / n * sum((Y[i] - Y_pred[i]) * X[i] for i in range(n))
        theta_0 -= learning_rate * d_theta_0
        theta_1 -= learning_rate * d_theta_1
    return theta_0, theta_1

# Function to fit the linear regression model
def fit_linear_regression(X, Y, learning_rate=0.01, iterations=1000):
    mean_X = calculate_mean(X)
    mean_Y = calculate_mean(Y)
    
    theta_1 = calculate_slope(X, Y, mean_X, mean_Y)
    theta_0 = calculate_intercept(mean_X, mean_Y, theta_1)
    
    theta_0, theta_1 = gradient_descent(X, Y, theta_0, theta_1, learning_rate, iterations)
    return theta_0, theta_1

# Function to test the model
def test_model():
    # Dataset
    experience = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    salary = [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000]
l
    theta_0, theta_1 = fit_linear_regression(experience, salary, learning_rate=0.01, iterations=1000)

 
    salary_pred = predict(experience, theta_0, theta_1)


    mse = calculate_mse(salary, salary_pred)

    print("Optimal Intercept (theta_0):", round(theta_0, 2))
    print("Optimal Slope (theta_1):", round(theta_1, 2))
    print("Mean Squared Error (MSE):", round(mse, 2))
    print("Predicted Salaries:", salary_pred)

# Run the model testing
test_model()
