import os
import gzip
import pickle
import random
import numpy as np


# ---------------------------
# 1. Load dataset
# ---------------------------
def load_mnist(path="mnist.pkl"):
    """Load the MNIST pickle file used in the lab."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Cannot find {path}")

    if path.endswith(".gz"):
        with gzip.open(path, "rb") as f:
            return pickle.load(f, encoding="latin1")
    else:
        with open(path, "rb") as f:
            return pickle.load(f, encoding="latin1")


# ---------------------------
# 2. Unpack train / validation / test
# ---------------------------
def get_train_test_splits(mnist):
    """Unpack MNIST tuple structure: (train, validation, test)."""
    train_data, validation_data, test_data = mnist
    train_features, train_labels = train_data
    val_features, val_labels = validation_data
    test_features, test_labels = test_data
    return train_features, train_labels, val_features, val_labels, test_features, test_labels


# ---------------------------
# 3. Build one-vs-all dataset
# ---------------------------
def create_one_vs_all_dataset(features, labels, target_digit):
    """
    Positive class  (+1): label == target_digit
    Negative class  (-1): label != target_digit
    """
    positive_examples = features[labels == target_digit]
    negative_examples = features[labels != target_digit]
    binary_labels = np.where(labels == target_digit, 1, -1)
    return positive_examples, negative_examples, binary_labels


# ---------------------------
# 4. Perceptron training for binary classification
# ---------------------------
def train_perceptron(positive_examples, negative_examples, num_iterations=1000, seed=42):
    """
    Train one binary perceptron.

    Output score rule:
    - positive sample should have score >= 0
    - negative sample should have score < 0
    """
    random.seed(seed)
    np.random.seed(seed)

    num_dims = positive_examples.shape[1]
    weights = np.zeros((num_dims, 1), dtype=np.float32)

    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        # If a positive example is classified incorrectly, move weights toward it.
        pos_score = np.dot(pos, weights).item()
        if pos_score < 0:
            weights = weights + pos.reshape(num_dims, 1)

        # If a negative example is classified incorrectly, move weights away from it.
        neg_score = np.dot(neg, weights).item()
        if neg_score >= 0:
            weights = weights - neg.reshape(num_dims, 1)

    return weights


# ---------------------------
# 5. Prediction helpers
# ---------------------------
def predict_binary(features, weights):
    """Return +1 or -1 for each sample."""
    scores = np.dot(features, weights).reshape(-1)
    return np.where(scores >= 0, 1, -1)


# ---------------------------
# 6. Accuracy for one-vs-all binary task
# ---------------------------
def binary_accuracy(features, labels, weights, target_digit):
    """
    Compare predicted binary labels to true one-vs-all binary labels.
    """
    true_binary_labels = np.where(labels == target_digit, 1, -1)
    predicted_binary_labels = predict_binary(features, weights)
    accuracy = np.mean(predicted_binary_labels == true_binary_labels)
    return accuracy, predicted_binary_labels, true_binary_labels


# ---------------------------
# 7. Main demo for one digit
# ---------------------------
def main():
    # Change this to "mnist.pkl" if that is the file you have locally.
    mnist = load_mnist("mnist.pkl")

    (
        train_features,
        train_labels,
        val_features,
        val_labels,
        test_features,
        test_labels,
    ) = get_train_test_splits(mnist)

    target_digit = 3
    print(f"=== Step 5: Train one perceptron for digit {target_digit} vs all ===")

    positive_examples, negative_examples, _ = create_one_vs_all_dataset(
        train_features, train_labels, target_digit
    )

    print("Training data summary:")
    print("  Train features shape:", train_features.shape)
    print("  Train labels shape:", train_labels.shape)
    print("  Positive examples shape:", positive_examples.shape)
    print("  Negative examples shape:", negative_examples.shape)

    weights = train_perceptron(
        positive_examples=positive_examples,
        negative_examples=negative_examples,
        num_iterations=1000,
        seed=42,
    )

    print("\nTraining complete.")
    print("Weights shape:", weights.shape)

    train_acc, train_pred, train_true = binary_accuracy(
        train_features, train_labels, weights, target_digit
    )
    test_acc, test_pred, test_true = binary_accuracy(
        test_features, test_labels, weights, target_digit)

    print(f"\nBinary accuracy for digit {target_digit} vs all:")
    print(f"  Train accuracy: {train_acc:.4f}")
    print(f"  Test accuracy:  {test_acc:.4f}")

    print("\nFirst 20 training predictions:")
    for i in range(20):
        print(
            f"Index {i:2d} | original label = {train_labels[i]} | "
            f"true binary = {train_true[i]:2d} | predicted binary = {train_pred[i]:2d}"
        )

    print("\nInterpretation:")
    print("  +1 means the model thinks the image IS the target digit.")
    print("  -1 means the model thinks the image is NOT the target digit.")
    print("  This is still only a binary classifier.")
    print("  In the next step, you will train 10 such perceptrons and combine them into one multi-class classifier.")


if __name__ == "__main__":
    main()
