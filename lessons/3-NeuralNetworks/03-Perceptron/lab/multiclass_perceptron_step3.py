import os
import pickle
import gzip
import numpy as np
import matplotlib.pyplot as plt


def load_mnist(path="mnist.pkl"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Cannot find {path}")

    if path.endswith(".gz"):
        with gzip.open(path, "rb") as f:
            return pickle.load(f, encoding="latin1")
    else:
        with open(path, "rb") as f:
            return pickle.load(f, encoding="latin1")


def inspect_split(name, features, labels):
    print(f"\n{name} split:")
    print("  Features type:", type(features))
    print("  Labels type:", type(labels))
    print("  Features shape:", features.shape)
    print("  Labels shape:", labels.shape)
    print("  First label:", labels[0])


def main():
    # Change this if your file is mnist.pkl instead of mnist.pkl.gz
    mnist = load_mnist("mnist.pkl")

    print("Type of mnist object:", type(mnist))
    print("Number of top-level items:", len(mnist))

    train_data, validation_data, test_data = mnist
    train_features, train_labels = train_data
    val_features, val_labels = validation_data
    test_features, test_labels = test_data

    inspect_split("Train", train_features, train_labels)
    inspect_split("Validation", val_features, val_labels)
    inspect_split("Test", test_features, test_labels)

    print("\nUnique labels in training set:", sorted(set(train_labels.tolist())))
    print("Feature vector length:", train_features.shape[1])

    sample_index = 0
    print("\nDisplaying one sample image...")
    print("Sample label:", train_labels[sample_index])

    plt.imshow(train_features[sample_index].reshape(28, 28), cmap="gray")
    plt.title(f"Label: {train_labels[sample_index]}")
    plt.show()


if __name__ == "__main__":
    main()