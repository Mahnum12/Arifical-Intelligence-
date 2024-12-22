import math
import random
from collections import Counter

def calculate_entropy(data, target_col):
    target_values = [row[target_col] for row in data]
    counter = Counter(target_values)
    total = len(target_values)
    entropy = -sum((count / total) * math.log2(count / total) for count in counter.values())
    return entropy


def calculate_information_gain(data, attribute, target_col):
    total_entropy = calculate_entropy(data, target_col)
    attribute_values = set(row[attribute] for row in data)
    total = len(data)
    weighted_entropy = 0
    for value in attribute_values:
        subset = [row for row in data if row[attribute] == value]
        weighted_entropy += (len(subset) / total) * calculate_entropy(subset, target_col)
    return total_entropy - weighted_entropy


def build_tree(data, attributes, target_col, depth=0, max_depth=3):
    if depth == max_depth or len(set(row[target_col] for row in data)) == 1:
  
        return Counter(row[target_col] for row in data).most_common(1)[0][0]
    
    best_attr = max(attributes, key=lambda attr: calculate_information_gain(data, attr, target_col))
    tree = {best_attr: {}}
    for value in set(row[best_attr] for row in data):
        subset = [row for row in data if row[best_attr] == value]
        tree[best_attr][value] = build_tree(subset, attributes - {best_attr}, target_col, depth + 1, max_depth)
    return tree

def predict(tree, data_point):
    if not isinstance(tree, dict):
        return tree
    attribute = next(iter(tree))
    value = data_point.get(attribute)
    return predict(tree[attribute].get(value, None), data_point)


def build_random_forest(data, attributes, target_col, n_trees=2):
    trees = []
    for _ in range(n_trees):
        sample = random.sample(data, len(data))
        tree = build_tree(sample, attributes, target_col)
        trees.append(tree)
    return trees


def predict_forest(forest, data_point):
    predictions = [predict(tree, data_point) for tree in forest]
    return Counter(predictions).most_common(1)[0][0]


dataset = [
    {'Weather': 'Sunny', 'Temperature': 'Hot', 'Play?': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Hot', 'Play?': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Mild', 'Play?': 'Yes'},
    {'Weather': 'Sunny', 'Temperature': 'Mild', 'Play?': 'No'},
    {'Weather': 'Overcast', 'Temperature': 'Mild', 'Play?': 'Yes'},
    {'Weather': 'Rainy', 'Temperature': 'Hot', 'Play?': 'No'}
]

attributes = {'Weather', 'Temperature'}
target_col = 'Play?'

forest = build_random_forest(dataset, attributes, target_col)

new_data = {'Weather': 'Sunny', 'Temperature': 'Hot'}
print("Prediction:", predict_forest(forest, new_data))
