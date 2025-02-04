
def calculate_mean(values):
    return sum(values) / len(values)


def calculate_slope(X, Y, mean_X, mean_Y):
    numerator = sum((x - mean_X) * (y - mean_Y) for x, y in zip(X, Y))
    denominator = sum((x - mean_X) ** 2 for x in X)
    return numerator / denominator


def calculate_intercept(mean_X, mean_Y, slope):
    return mean_Y - slope * mean_X


def predict(X, intercept, slope):
    return [intercept + slope * x for x in X]


def calculate_mse(Y, Y_pred):
    return sum((y - y_pred) ** 2 for y, y_pred in zip(Y, Y_pred)) / len(Y)


def fit_linear_regression(X, Y):
    mean_X = calculate_mean(X)
    mean_Y = calculate_mean(Y)
    slope = calculate_slope(X, Y, mean_X, mean_Y)
    intercept = calculate_intercept(mean_X, mean_Y, slope)
    return intercept, slope


X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 7, 8]


intercept, slope = fit_linear_regression(X, Y)


Y_pred = predict(X, intercept, slope)


mse = calculate_mse(Y, Y_pred)

print("Intercept:", intercept)
print("Slope:", slope)
print("Predictions:", Y_pred)
print("Mean Squared Error:", mse)
