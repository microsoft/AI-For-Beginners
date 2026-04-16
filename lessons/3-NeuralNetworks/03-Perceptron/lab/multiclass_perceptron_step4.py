import os
import gzip
import pickle
import numpy as np
import matplotlib.pyplot as plt


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


def get_train_test_splits(mnist):
    """Unpack the tuple structure: (train, validation, test)."""
    train_data, validation_data, test_data = mnist
    train_features, train_labels = train_data
    val_features, val_labels = validation_data
    test_features, test_labels = test_data
    return train_features, train_labels, val_features, val_labels, test_features, test_labels


def create_one_vs_all_dataset(features, labels, target_digit):
    """
    Build a binary dataset for one-vs-all classification.

    Positive class  (+1): all images whose label == target_digit
    Negative class  (-1): all images whose label != target_digit
    """
    positive_mask = labels == target_digit
    negative_mask = labels != target_digit

    positive_examples = features[positive_mask]
    negative_examples = features[negative_mask]

    # Binary labels are often helpful for checking or later evaluation.
    binary_labels = np.where(labels == target_digit, 1, -1)

    return positive_examples, negative_examples, binary_labels


def inspect_one_vs_all(features, labels, target_digit):
    """Print useful information for the chosen target digit."""
    positive_examples, negative_examples, binary_labels = create_one_vs_all_dataset(
        features, labels, target_digit
    )

    print(f"\n=== One-vs-All dataset for digit {target_digit} ===")
    print("Original feature matrix shape:", features.shape)
    print("Original label vector shape:", labels.shape)
    print("Positive examples shape:", positive_examples.shape)
    print("Negative examples shape:", negative_examples.shape)
    print("Binary labels shape:", binary_labels.shape)
    print("Positive count:", len(positive_examples))
    print("Negative count:", len(negative_examples))

    print("\nFirst 20 original labels:")
    print(labels[:20])
    print("\nFirst 20 binary labels (+1 means target digit, -1 means all others):")
    print(binary_labels[:20])

    return positive_examples, negative_examples, binary_labels


def show_example_images(positive_examples, negative_examples, target_digit):
    """Display one positive and one negative example for visual checking."""
    plt.figure(figsize=(6, 3))

    plt.subplot(1, 2, 1)
    plt.imshow(positive_examples[0].reshape(28, 28), cmap="gray")
    plt.title(f"Positive: {target_digit}")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(negative_examples[0].reshape(28, 28), cmap="gray")
    plt.title(f"Negative: not {target_digit}")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


def main():
    # Change the filename here if your local file is mnist.pkl instead of mnist.pkl.gz
    mnist = load_mnist("mnist.pkl")

    train_features, train_labels, val_features, val_labels, test_features, test_labels = get_train_test_splits(mnist)

    # For Step 4, start with one target digit to understand the structure.
    target_digit = 6

    positive_examples, negative_examples, binary_labels = inspect_one_vs_all(
        train_features, train_labels, target_digit
    )

    print("\nChecking a few labels manually:")
    for i in range(10):
        print(
            f"Index {i}: original label = {train_labels[i]}, binary label = {binary_labels[i]}"
        )

    show_example_images(positive_examples, negative_examples, target_digit)

    print("\nStep 4 complete.")
    print(
        "You now have a function that converts the original multi-class MNIST data into a binary one-vs-all dataset."
    )
    print(
        "The next step will be to train one perceptron for one target digit, then repeat that for all 10 digits."
    )


if __name__ == "__main__":
    main()
