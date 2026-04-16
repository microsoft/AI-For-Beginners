import os
import gzip
import pickle
import numpy as np

"""
Step 7: Evaluate the full multi-class perceptron model with a confusion matrix.

This script extends Step 6 by:
1. training 10 one-vs-all perceptrons,
2. predicting digits on train and test sets,
3. computing train and test accuracy,
4. printing confusion matrices,
5. showing per-class accuracy to make errors easier to interpret.
"""


def load_mnist(path=None):
    """Load the MNIST pickle file used in the original lab."""
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
    """Unpack (train, validation, test) splits from the Nielsen MNIST pickle."""
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
    return x / 255.0



def add_bias_column(x):
    ones = np.ones((x.shape[0], 1), dtype=np.float32)
    return np.hstack([x, ones])



def create_one_vs_all_labels(labels, target_digit):
    return np.where(labels == target_digit, 1, -1).astype(np.int64)



def train_binary_perceptron(x_aug, y, num_epochs=10):
    """Batch perceptron training for binary labels in {-1, +1}."""
    w = np.zeros(x_aug.shape[1], dtype=np.float32)
    history = []

    for epoch in range(1, num_epochs + 1):
        scores = x_aug @ w
        margins = y * scores
        misclassified_mask = margins <= 0
        misclassified_count = int(np.sum(misclassified_mask))
        binary_accuracy = float(np.mean(np.where(scores >= 0, 1, -1) == y))
        history.append((epoch, misclassified_count, binary_accuracy))

        if misclassified_count == 0:
            break

        w += (y[misclassified_mask, None] * x_aug[misclassified_mask]).sum(axis=0)

    return w, history



def train_all_perceptrons(train_features, train_labels, num_epochs=10):
    """Train one perceptron for each digit 0-9."""
    x_norm = normalize_features(train_features)
    x_aug = add_bias_column(x_norm)

    weight_matrix = np.zeros((10, x_aug.shape[1]), dtype=np.float32)
    histories = {}

    for digit in range(10):
        print(f"\nTraining digit {digit} vs all...")
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
    x_norm = normalize_features(features)
    x_aug = add_bias_column(x_norm)
    return x_aug @ weight_matrix.T



def predict_digits(features, weight_matrix):
    scores = compute_scores(features, weight_matrix)
    return np.argmax(scores, axis=1)



def multiclass_accuracy(true_labels, predicted_labels):
    return float(np.mean(true_labels == predicted_labels))



def confusion_matrix(true_labels, predicted_labels, num_classes=10):
    """Build a confusion matrix where rows=true class and cols=predicted class."""
    matrix = np.zeros((num_classes, num_classes), dtype=np.int64)
    for true_digit, pred_digit in zip(true_labels, predicted_labels):
        matrix[int(true_digit), int(pred_digit)] += 1
    return matrix



def print_confusion_matrix(matrix, title="Confusion Matrix"):
    print(f"\n{title}")
    print("rows = true labels, columns = predicted labels")

    header = "     " + " ".join([f"{i:5d}" for i in range(matrix.shape[1])])
    print(header)
    print("    " + "-" * (6 * matrix.shape[1]))

    for i, row in enumerate(matrix):
        row_text = " ".join([f"{value:5d}" for value in row])
        print(f"{i:2d} | {row_text}")



def per_class_accuracy(matrix):
    """Return accuracy for each true digit based on the confusion matrix."""
    class_acc = {}
    for digit in range(matrix.shape[0]):
        total = int(np.sum(matrix[digit]))
        correct = int(matrix[digit, digit])
        acc = correct / total if total > 0 else 0.0
        class_acc[digit] = (correct, total, acc)
    return class_acc



def print_per_class_accuracy(class_acc, title="Per-class accuracy"):
    print(f"\n{title}")
    print(" digit | correct / total | accuracy")
    print("-" * 38)
    for digit, (correct, total, acc) in class_acc.items():
        print(f" {digit:5d} | {correct:7d} / {total:5d} | {acc:.4f}")



def print_sample_predictions(true_labels, predicted_labels, count=15):
    print("\nSample test predictions")
    print(" index | true digit | predicted digit | correct?")
    print("-" * 48)
    for i in range(min(count, len(true_labels))):
        correct = "yes" if true_labels[i] == predicted_labels[i] else "no"
        print(f" {i:5d} | {true_labels[i]:10d} | {predicted_labels[i]:15d} | {correct}")



def main():
    print("Step 7 - Multi-class evaluation with confusion matrix")

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

    weight_matrix, histories = train_all_perceptrons(
        train_features, train_labels, num_epochs=10
    )

    train_predictions = predict_digits(train_features, weight_matrix)
    test_predictions = predict_digits(test_features, weight_matrix)

    train_acc = multiclass_accuracy(train_labels, train_predictions)
    test_acc = multiclass_accuracy(test_labels, test_predictions)

    print("\nOverall results")
    print(f"Training accuracy: {train_acc:.4f}")
    print(f"Test accuracy:     {test_acc:.4f}")
    print("Weight matrix shape:", weight_matrix.shape)

    train_cm = confusion_matrix(train_labels, train_predictions)
    test_cm = confusion_matrix(test_labels, test_predictions)

    print_confusion_matrix(train_cm, title="Training confusion matrix")
    print_confusion_matrix(test_cm, title="Test confusion matrix")

    train_class_acc = per_class_accuracy(train_cm)
    test_class_acc = per_class_accuracy(test_cm)

    print_per_class_accuracy(train_class_acc, title="Training per-class accuracy")
    print_per_class_accuracy(test_class_acc, title="Test per-class accuracy")

    print_sample_predictions(test_labels, test_predictions, count=15)

    print("\nStep 7 complete.")
    print("This script now covers the evaluation part requested by the lab:")
    print("- multi-class train/test accuracy")
    print("- confusion matrix")


if __name__ == "__main__":
    main()
