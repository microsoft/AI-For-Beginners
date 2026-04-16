import argparse
import csv
import gzip
import os
import pickle
from typing import Dict, List, Optional, Tuple

import numpy as np


"""
Step 8: Final clean submission version for the multi-class perceptron lab.

This script:
1. loads the MNIST pickle file used in the lab,
2. trains 10 one-vs-all perceptrons,
3. predicts digits with argmax over all perceptron scores,
4. computes train / validation / test accuracy,
5. prints confusion matrices,
6. saves confusion matrices as CSV files.

Why this version exists:
- keeps the original notebook untouched,
- combines the full lab solution into one clean Python file,
- is easier to run top-to-bottom when preparing for submission.
"""


# ---------- Data loading ----------

def load_mnist(path: Optional[str] = None):
    """Load the Nielsen-style MNIST pickle in Python 3."""
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



def unpack_mnist(mnist) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Unpack the (train, validation, test) tuple returned by the MNIST pickle."""
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


# ---------- Preprocessing ----------

def normalize_features(features: np.ndarray) -> np.ndarray:
    """Scale pixel values to a smaller range for more stable learning."""
    return features / 255.0



def add_bias_column(features: np.ndarray) -> np.ndarray:
    """Append a bias column of ones so bias becomes part of the weight vector."""
    ones = np.ones((features.shape[0], 1), dtype=np.float32)
    return np.hstack([features, ones])



def prepare_features(features: np.ndarray) -> np.ndarray:
    """Normalize and augment the feature matrix with a bias column."""
    return add_bias_column(normalize_features(features))



def create_one_vs_all_labels(labels: np.ndarray, target_digit: int) -> np.ndarray:
    """Return binary labels: +1 for target digit, -1 for all other digits."""
    return np.where(labels == target_digit, 1, -1).astype(np.int64)


# ---------- Perceptron training ----------

def train_binary_perceptron(
    features_aug: np.ndarray,
    binary_labels: np.ndarray,
    num_epochs: int = 10,
) -> Tuple[np.ndarray, List[Tuple[int, int, float]]]:
    """
    Train a binary perceptron using batch-style updates.

    Returns:
        weights: learned weight vector
        history: list of (epoch, misclassified_count, binary_accuracy)
    """
    weights = np.zeros(features_aug.shape[1], dtype=np.float32)
    history: List[Tuple[int, int, float]] = []

    for epoch in range(1, num_epochs + 1):
        scores = features_aug @ weights
        margins = binary_labels * scores
        misclassified_mask = margins <= 0
        misclassified_count = int(np.sum(misclassified_mask))

        predicted_binary = np.where(scores >= 0, 1, -1)
        binary_accuracy = float(np.mean(predicted_binary == binary_labels))
        history.append((epoch, misclassified_count, binary_accuracy))

        if misclassified_count == 0:
            break

        weights += (
            binary_labels[misclassified_mask, None] * features_aug[misclassified_mask]
        ).sum(axis=0)

    return weights, history



def train_all_perceptrons(
    train_features: np.ndarray,
    train_labels: np.ndarray,
    num_epochs: int = 10,
) -> Tuple[np.ndarray, Dict[int, List[Tuple[int, int, float]]]]:
    """Train one one-vs-all perceptron for each digit 0-9."""
    train_aug = prepare_features(train_features)
    weight_matrix = np.zeros((10, train_aug.shape[1]), dtype=np.float32)
    histories: Dict[int, List[Tuple[int, int, float]]] = {}

    for digit in range(10):
        binary_labels = create_one_vs_all_labels(train_labels, digit)
        weights, history = train_binary_perceptron(train_aug, binary_labels, num_epochs)
        weight_matrix[digit] = weights
        histories[digit] = history

    return weight_matrix, histories


# ---------- Prediction ----------

def compute_scores(features: np.ndarray, weight_matrix: np.ndarray) -> np.ndarray:
    """Compute all 10 perceptron scores at once."""
    features_aug = prepare_features(features)
    return features_aug @ weight_matrix.T



def predict_digits(features: np.ndarray, weight_matrix: np.ndarray) -> np.ndarray:
    """Predict the digit by selecting the largest perceptron score."""
    scores = compute_scores(features, weight_matrix)
    return np.argmax(scores, axis=1)


# ---------- Evaluation ----------

def multiclass_accuracy(true_labels: np.ndarray, predicted_labels: np.ndarray) -> float:
    return float(np.mean(true_labels == predicted_labels))



def confusion_matrix(
    true_labels: np.ndarray,
    predicted_labels: np.ndarray,
    num_classes: int = 10,
) -> np.ndarray:
    matrix = np.zeros((num_classes, num_classes), dtype=np.int64)
    for true_digit, pred_digit in zip(true_labels, predicted_labels):
        matrix[int(true_digit), int(pred_digit)] += 1
    return matrix



def per_class_accuracy(matrix: np.ndarray) -> Dict[int, Tuple[int, int, float]]:
    results: Dict[int, Tuple[int, int, float]] = {}
    for digit in range(matrix.shape[0]):
        total = int(np.sum(matrix[digit]))
        correct = int(matrix[digit, digit])
        accuracy = correct / total if total > 0 else 0.0
        results[digit] = (correct, total, accuracy)
    return results



def top_confusions(matrix: np.ndarray, top_k: int = 10) -> List[Tuple[int, int, int]]:
    """Return the largest off-diagonal confusion counts."""
    confusions: List[Tuple[int, int, int]] = []
    for true_digit in range(matrix.shape[0]):
        for pred_digit in range(matrix.shape[1]):
            if true_digit != pred_digit:
                confusions.append((true_digit, pred_digit, int(matrix[true_digit, pred_digit])))
    confusions.sort(key=lambda item: item[2], reverse=True)
    return confusions[:top_k]


# ---------- Reporting ----------

def print_dataset_summary(
    train_features: np.ndarray,
    train_labels: np.ndarray,
    val_features: np.ndarray,
    val_labels: np.ndarray,
    test_features: np.ndarray,
    test_labels: np.ndarray,
) -> None:
    print("Dataset summary")
    print("-" * 60)
    print("Train features shape:     ", train_features.shape)
    print("Train labels shape:       ", train_labels.shape)
    print("Validation features shape:", val_features.shape)
    print("Validation labels shape:  ", val_labels.shape)
    print("Test features shape:      ", test_features.shape)
    print("Test labels shape:        ", test_labels.shape)
    print("Unique training labels:   ", sorted(set(train_labels.tolist())))
    print()



def print_training_summary(histories: Dict[int, List[Tuple[int, int, float]]]) -> None:
    print("Training summary by digit")
    print("-" * 60)
    print(" digit | last epoch | misclassified | binary accuracy")
    print("-" * 60)
    for digit in range(10):
        last_epoch, last_errors, last_acc = histories[digit][-1]
        print(f" {digit:5d} | {last_epoch:10d} | {last_errors:13d} | {last_acc:.4f}")
    print()



def print_confusion_matrix(matrix: np.ndarray, title: str) -> None:
    print(title)
    print("rows = true labels, columns = predicted labels")
    header = "     " + " ".join([f"{i:5d}" for i in range(matrix.shape[1])])
    print(header)
    print("    " + "-" * (6 * matrix.shape[1]))
    for row_index, row in enumerate(matrix):
        row_text = " ".join([f"{value:5d}" for value in row])
        print(f"{row_index:2d} | {row_text}")
    print()



def print_per_class_accuracy(class_results: Dict[int, Tuple[int, int, float]], title: str) -> None:
    print(title)
    print(" digit | correct / total | accuracy")
    print("-" * 40)
    for digit, (correct, total, accuracy) in class_results.items():
        print(f" {digit:5d} | {correct:7d} / {total:5d} | {accuracy:.4f}")
    print()



def print_top_confusions(confusions: List[Tuple[int, int, int]], title: str) -> None:
    print(title)
    print(" true digit | predicted digit | count")
    print("-" * 40)
    for true_digit, pred_digit, count in confusions:
        print(f" {true_digit:10d} | {pred_digit:15d} | {count:5d}")
    print()



def save_matrix_to_csv(matrix: np.ndarray, file_path: str) -> None:
    with open(file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["true\\pred"] + list(range(matrix.shape[1])))
        for row_index, row in enumerate(matrix):
            writer.writerow([row_index] + row.tolist())


# ---------- Main ----------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Final multi-class perceptron solution for the MNIST lab"
    )
    parser.add_argument(
        "--data",
        type=str,
        default=None,
        help="Path to mnist.pkl.gz or mnist.pkl. If omitted, the script tries both automatically.",
    )
    parser.add_argument(
        "--epochs",
        type=int,
        default=10,
        help="Number of perceptron training epochs for each one-vs-all classifier.",
    )
    parser.add_argument(
        "--save-dir",
        type=str,
        default=".",
        help="Folder where confusion matrix CSV files will be saved.",
    )
    return parser.parse_args()



def main() -> None:
    args = parse_args()

    print("Step 8 - Final clean submission version")
    print("=" * 60)

    mnist = load_mnist(args.data)
    (
        train_features,
        train_labels,
        val_features,
        val_labels,
        test_features,
        test_labels,
    ) = unpack_mnist(mnist)

    print_dataset_summary(
        train_features,
        train_labels,
        val_features,
        val_labels,
        test_features,
        test_labels,
    )

    weight_matrix, histories = train_all_perceptrons(
        train_features, train_labels, num_epochs=args.epochs
    )

    print_training_summary(histories)

    train_predictions = predict_digits(train_features, weight_matrix)
    val_predictions = predict_digits(val_features, weight_matrix)
    test_predictions = predict_digits(test_features, weight_matrix)

    train_accuracy = multiclass_accuracy(train_labels, train_predictions)
    val_accuracy = multiclass_accuracy(val_labels, val_predictions)
    test_accuracy = multiclass_accuracy(test_labels, test_predictions)

    print("Overall multi-class accuracy")
    print("-" * 60)
    print(f"Training accuracy:   {train_accuracy:.4f}")
    print(f"Validation accuracy: {val_accuracy:.4f}")
    print(f"Test accuracy:       {test_accuracy:.4f}")
    print("Weight matrix shape: ", weight_matrix.shape)
    print()

    train_cm = confusion_matrix(train_labels, train_predictions)
    val_cm = confusion_matrix(val_labels, val_predictions)
    test_cm = confusion_matrix(test_labels, test_predictions)

    print_confusion_matrix(train_cm, "Training confusion matrix")
    print_confusion_matrix(val_cm, "Validation confusion matrix")
    print_confusion_matrix(test_cm, "Test confusion matrix")

    print_per_class_accuracy(per_class_accuracy(train_cm), "Training per-class accuracy")
    print_per_class_accuracy(per_class_accuracy(val_cm), "Validation per-class accuracy")
    print_per_class_accuracy(per_class_accuracy(test_cm), "Test per-class accuracy")

    print_top_confusions(top_confusions(test_cm, top_k=10), "Top test confusions")

    os.makedirs(args.save_dir, exist_ok=True)
    train_csv_path = os.path.join(args.save_dir, "train_confusion_matrix.csv")
    val_csv_path = os.path.join(args.save_dir, "validation_confusion_matrix.csv")
    test_csv_path = os.path.join(args.save_dir, "test_confusion_matrix.csv")

    save_matrix_to_csv(train_cm, train_csv_path)
    save_matrix_to_csv(val_cm, val_csv_path)
    save_matrix_to_csv(test_cm, test_csv_path)

    print("Saved files")
    print("-" * 60)
    print("Train confusion matrix CSV:     ", train_csv_path)
    print("Validation confusion matrix CSV:", val_csv_path)
    print("Test confusion matrix CSV:      ", test_csv_path)
    print()

    print("Step 8 complete.")
    print("This file is the cleaned final version of the lab pipeline:")
    print("- one-vs-all training for digits 0-9")
    print("- multi-class prediction with argmax")
    print("- train / validation / test accuracy")
    print("- confusion matrices")


if __name__ == "__main__":
    main()
