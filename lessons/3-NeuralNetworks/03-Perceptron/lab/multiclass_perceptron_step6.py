import os
import gzip
import pickle
import numpy as np


"""
Step 6: Train all 10 one-vs-all perceptrons and build the first
full multi-class digit classifier.

This script keeps the original notebook untouched.
It trains one binary perceptron for each digit (0-9):
    digit 0 vs all others
    digit 1 vs all others
    ...
    digit 9 vs all others

Then it combines the 10 trained perceptrons into one weight matrix and
predicts the final class by choosing the digit with the highest score.
"""


def load_mnist(path=None):
    """Load the MNIST pickle file used in the original lab.

    The common files for this lab are:
    - mnist.pkl.gz
    - mnist.pkl

    The file was usually serialized with Python 2, so Python 3 needs
    encoding='latin1'.
    """
    candidates = [path] if path else ["mnist.pkl.gz", "mnist.pkl"]

    for candidate in candidates:
        if candidate and os.path.exists(candidate):
            if candidate.endswith(".gz"):
                with gzip.open(candidate, "rb") as f:
                    return pickle.load(f, encoding="latin1")
            with open(candidate, "rb") as f:
                return pickle.load(f, encoding="latin1")

    raise FileNotFoundError(
        "Could not find mnist.pkl.gz or mnist.pkl in the current folder."
    )



def unpack_mnist(mnist):
    """Unpack the dataset into train / validation / test splits.

    Format from the MNIST lab:
        mnist = (train_data, validation_data, test_data)
        train_data = (train_features, train_labels)
    """
    train_data, validation_data, test_data = mnist
    train_features, train_labels = train_data
    val_features, val_labels = validation_data
    test_features, test_labels = test_data

    return (
        np.asarray(train_features, dtype=np.float32),
        np.asarray(train_labels, dtype=np.int64),
        np.asarray(val_features, dtype=np.float32),
        np.asarray(val_labels, dtype=np.int64),
        np.asarray(test_features, dtype=np.float32),
        np.asarray(test_labels, dtype=np.int64),
    )



def normalize_features(x):
    """Normalize pixel values to approximately [0, 1]."""
    return x / 255.0



def add_bias_column(x):
    """Append a bias term of 1 to every sample.

    If x has shape (n_samples, n_features), the output becomes:
        (n_samples, n_features + 1)
    """
    ones = np.ones((x.shape[0], 1), dtype=np.float32)
    return np.hstack([x, ones])



def create_one_vs_all_labels(labels, target_digit):
    """Return +1 for target_digit and -1 for all other digits."""
    return np.where(labels == target_digit, 1, -1).astype(np.int64)



def train_binary_perceptron(x_aug, y, num_epochs=10):
    """Train one binary perceptron using a vectorized batch update.

    Parameters
    ----------
    x_aug : np.ndarray
        Feature matrix with bias column already added.
    y : np.ndarray
        Labels in {-1, +1}
    num_epochs : int
        Number of passes over the dataset.

    Returns
    -------
    w : np.ndarray
        Weight vector with shape (n_features + 1,)
    history : list[tuple[int, int, float]]
        Each entry contains:
        (epoch_number, number_of_misclassified_samples, binary_accuracy)
    """
    w = np.zeros(x_aug.shape[1], dtype=np.float32)
    history = []

    for epoch in range(1, num_epochs + 1):
        scores = x_aug @ w
        margins = y * scores
        misclassified_mask = margins <= 0
        misclassified_count = int(np.sum(misclassified_mask))
        binary_accuracy = float(np.mean(np.sign(scores + 1e-12) == y))
        history.append((epoch, misclassified_count, binary_accuracy))

        if misclassified_count == 0:
            break

        # Batch perceptron update:
        # Sum y_i * x_i for all currently misclassified samples.
        w += (y[misclassified_mask, None] * x_aug[misclassified_mask]).sum(axis=0)

    return w, history



def train_all_perceptrons(train_features, train_labels, num_epochs=10):
    """Train 10 one-vs-all perceptrons and stack them into one matrix.

    Returns
    -------
    weight_matrix : np.ndarray
        Shape: (10, n_features + 1)
        Row i contains the weights for digit i vs all.
    histories : dict[int, list[tuple[int, int, float]]]
        Training history for each digit.
    """
    x_norm = normalize_features(train_features)
    x_aug = add_bias_column(x_norm)

    weight_matrix = np.zeros((10, x_aug.shape[1]), dtype=np.float32)
    histories = {}

    for digit in range(10):
        print(f"\nTraining perceptron for digit {digit} vs all...")
        y = create_one_vs_all_labels(train_labels, digit)
        weights, history = train_binary_perceptron(x_aug, y, num_epochs=num_epochs)
        weight_matrix[digit] = weights
        histories[digit] = history

        last_epoch, last_errors, last_acc = history[-1]
        print(
            f"  Finished at epoch {last_epoch} | "
            f"misclassified={last_errors} | binary accuracy={last_acc:.4f}"
        )

    return weight_matrix, histories



def compute_scores(features, weight_matrix):
    """Compute the score of every digit perceptron for every sample.

    Output shape:
        (n_samples, 10)
    """
    x_norm = normalize_features(features)
    x_aug = add_bias_column(x_norm)
    return x_aug @ weight_matrix.T



def predict_digits(features, weight_matrix):
    """Predict the digit by selecting the perceptron with the largest score."""
    scores = compute_scores(features, weight_matrix)
    return np.argmax(scores, axis=1)



def multiclass_accuracy(true_labels, predicted_labels):
    return float(np.mean(true_labels == predicted_labels))



def print_sample_predictions(features, true_labels, predicted_labels, count=15):
    print("\nSample multi-class predictions:")
    print(" index | true digit | predicted digit | correct?")
    print("-" * 48)
    for i in range(min(count, len(true_labels))):
        correct = "yes" if true_labels[i] == predicted_labels[i] else "no"
        print(f" {i:5d} | {true_labels[i]:10d} | {predicted_labels[i]:15d} | {correct}")



def main():
    print("Step 6 - Train all 10 one-vs-all perceptrons")

    mnist = load_mnist("mnist.pkl")
    (
        train_features,
        train_labels,
        val_features,
        val_labels,
        test_features,
        test_labels,
    ) = unpack_mnist(mnist)

    print("\nDataset summary")
    print("Train features shape:", train_features.shape)
    print("Train labels shape:  ", train_labels.shape)
    print("Validation features shape:", val_features.shape)
    print("Validation labels shape:  ", val_labels.shape)
    print("Test features shape:", test_features.shape)
    print("Test labels shape:  ", test_labels.shape)

    # Main training stage for Step 6
    weight_matrix, histories = train_all_perceptrons(
        train_features, train_labels, num_epochs=10
    )

    print("\nWeight matrix shape:", weight_matrix.shape)
    print("This should be (10, number_of_features + 1).")

    # First full multi-class prediction
    train_predictions = predict_digits(train_features, weight_matrix)
    test_predictions = predict_digits(test_features, weight_matrix)

    train_acc = multiclass_accuracy(train_labels, train_predictions)
    test_acc = multiclass_accuracy(test_labels, test_predictions)

    print("\nFirst full multi-class results")
    print(f"Training accuracy: {train_acc:.4f}")
    print(f"Test accuracy:     {test_acc:.4f}")

    print_sample_predictions(test_features, test_labels, test_predictions, count=15)

    print("\nStep 6 complete.")
    print("You now have 10 trained perceptrons and a multi-class predictor.")
    print("Next step: compute and display the confusion matrix in Step 7.")


if __name__ == "__main__":
    main()
