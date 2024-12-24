import numpy as np
import matplotlib.pyplot as plt


def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cross_entropy_loss(y_true, y_pred):
    y_pred = np.clip(y_pred, 1e-9, 1 - 1e-9)  
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))


def gradient_descent(X, y, weights, learning_rate, iterations):
    m = X.shape[0]
    for i in range(iterations):
        predictions = sigmoid(np.dot(X, weights))
        error = predictions - y
        gradient = np.dot(X.T, error) / m
        weights -= learning_rate * gradient
        
        if i % (iterations // 10) == 0:  
            loss = cross_entropy_loss(y, predictions)
            print(f"Iteration {i}: Loss = {loss:.4f}")
    return weights


def predict(X, weights):
    return (sigmoid(np.dot(X, weights)) >= 0.5).astype(int)


def logistic_regression(X, y, learning_rate=0.01, iterations=1000):
    X = np.c_[np.ones(X.shape[0]), X]  
    weights = np.zeros(X.shape[1])
    weights = gradient_descent(X, y, weights, learning_rate, iterations)
    return weights


def evaluate(y_true, y_pred):
    accuracy = np.mean(y_true == y_pred) * 100
    return accuracy


def plot_decision_boundary(X, y, weights):
    x_values = [np.min(X[:, 0]) - 1, np.max(X[:, 0]) + 1]
    y_values = -(weights[0] + np.dot(weights[1], x_values)) / weights[2]
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
    plt.plot(x_values, y_values, label="Decision Boundary")
    plt.xlabel('Feature 1 (X1)')
    plt.ylabel('Feature 2 (X2)')
    plt.legend()
    plt.show()

data = np.array([
    [0.1, 1.1, 0],
    [1.2, 0.9, 0],
    [1.5, 1.6, 1],
    [2.0, 1.8, 1],
    [2.5, 2.1, 1],
    [0.5, 1.5, 0],
    [1.8, 2.3, 1],
    [0.2, 0.7, 0],
    [1.9, 1.4, 1],
    [0.8, 0.6, 0]
])
X = data[:, :2]
y = data[:, 2]

X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X_standardized = (X - X_mean) / X_std

plt.scatter(X_standardized[:, 0], X_standardized[:, 1], c=y, cmap='viridis')
plt.xlabel('Feature 1 (X1)')
plt.ylabel('Feature 2 (X2)')
plt.title('Data Distribution')
plt.show()

learning_rate = 0.1
iterations = 1000
weights = logistic_regression(X_standardized, y, learning_rate, iterations)


X_with_bias = np.c_[np.ones(X_standardized.shape[0]), X_standardized]
y_pred = predict(X_with_bias, weights)

accuracy = evaluate(y, y_pred)
loss = cross_entropy_loss(y, sigmoid(np.dot(X_with_bias, weights)))
print(f"Model Accuracy: {accuracy:.2f}%")
print(f"Cross-Entropy Loss: {loss:.4f}")

plot_decision_boundary(X_standardized, y, weights)
