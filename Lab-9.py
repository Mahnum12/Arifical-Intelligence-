import math
from collections import Counter

def calculate_entropy(data, target_col):
    target_counts = Counter(data[target_col])
    total_count = len(data[target_col])
    entropy = 0
    for count in target_counts.values():
        p = count / total_count
        entropy -= p * math.log2(p)
    return entropy

def calculate_information_gain(data, attribute, target_col):
    parent_entropy = calculate_entropy(data, target_col)
    attribute_values = data[attribute]
    total_count = len(attribute_values)
    weighted_entropy = 0
    for value in set(attribute_values):
        subset = [i for i, val in enumerate(attribute_values) if val == value]
        subset_data = {key: [data[key][i] for i in subset] for key in data}
        subset_entropy = calculate_entropy(subset_data, target_col)
        weighted_entropy += (len(subset) / total_count) * subset_entropy
    return parent_entropy - weighted_entropy

def build_tree(data, attributes, target_col):
    if len(set(data[target_col])) == 1:  
        return data[target_col][0]
    if not attributes: 
        return Counter(data[target_col]).most_common(1)[0][0]
    
    gains = {attr: calculate_information_gain(data, attr, target_col) for attr in attributes}
    best_attr = max(gains, key=gains.get)
    tree = {best_attr: {}}
    remaining_attributes = [attr for attr in attributes if attr != best_attr]
    
    for value in set(data[best_attr]):
        subset = [i for i, val in enumerate(data[best_attr]) if val == value]
        subset_data = {key: [data[key][i] for i in subset] for key in data}
        tree[best_attr][value] = build_tree(subset_data, remaining_attributes, target_col)
    
    return tree

def predict(tree, data_point):
    if not isinstance(tree, dict):
        return tree  
    attribute = next(iter(tree))
    value = data_point.get(attribute)
    subtree = tree[attribute].get(value)
    if subtree is None:
        return None  
    return predict(subtree, data_point)

if __name__ == "__main__":

    data = {
        "Weather": ["Sunny", "Overcast", "Rainy", "Sunny", "Rainy"],
        "Temperature": ["Hot", "Hot", "Mild", "Mild", "Cool"],
        "Play?": ["No", "Yes", "Yes", "Yes", "No"]
    }
    target_col = "Play?"
    attributes = ["Weather", "Temperature"]

    decision_tree = build_tree(data, attributes, target_col)
    print("Decision Tree:", decision_tree)

    test_data = {"Weather": "Sunny", "Temperature": "Mild"}
    prediction = predict(decision_tree, test_data)
    print("Prediction for test data:", prediction)
