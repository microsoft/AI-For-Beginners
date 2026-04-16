import os
import pickle
import gzip
import numpy as np
import random
import matplotlib.pyplot as plt

def load_mnist(path=None):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Cannot find {path}")
    
    else:
        with open(path, "rb") as f:
            return pickle.load(f, encoding="latin1")

def get_train_test_splits(mnist):
    ## unpack tuple structure
    train_data, validation_data, test_data = mnist
    train_features, train_labels = train_data
    val_features, val_labels = validation_data
    test_features, test_labels = test_data
    return train_features, train_labels, val_features, val_labels, test_features, test_labels

def create_one_vs_all_dataset(features, labels, target):
    pos_ex = features[labels == target]
    nev_ex = features[labels != target]

    bin_labels = np.where(labels == target, 1, -1)

    return pos_ex, nev_ex, bin_labels

def train_perceptron(posEx, negEx, numIterations = 1000, seed = 42):
    random.seed(seed)
    np.random.seed(seed)

    numDims = posEx.shape[1]
    weights = np.zeros((numDims,1), dtype=np.float32)

    for i in range(numIterations):
        pos = random.choice(posEx)
        nev = random.choice(negEx)

        posScore = np.dot(pos, weights).item()
        if posScore < 0:
            weights = weights + pos.reshape(numDims,1)

        negScore = np.dot(nev,weights).item()
        if negScore >= 0:
            weights = weights - nev.reshape(numDims, 1)
            
    return weights

def predictBinary(features, weights):
    scores = np.dot(features,weights).reshape(-1)
    return np.where(scores >= 0,1,-1)

def binaryAccuracy(features, labels, weights, target):
    trueBinLabels = np.where(labels == target, 1, -1)
    predictedBinlabels = predictBinary(features, weights)
    accuracy = np.mean(predictedBinlabels == trueBinLabels)
    return accuracy, predictedBinlabels, trueBinLabels



def main():
    train_features, train_labels, val_features, val_labels, test_features, test_labels = get_train_test_splits(load_mnist("mnist.pkl"))

    target = 6
    print(f"===Train one perceptron for digit {target} vs all ===")

    posEx, negEx , _ = create_one_vs_all_dataset(
        train_features, train_labels, target
    )


    weights = train_perceptron(
        posEx=posEx,
        negEx = negEx,
        numIterations= 1000,
        seed=42
    )

    print("\nTraining complete")
    print("weights shape:", weights.shape)

    trainAcc, trainPred, trainTrue = binaryAccuracy(
        train_features, train_labels, weights, target
    )

    testAcc, testPred, testTrue = binaryAccuracy(
        test_features, test_labels, weights, target
    )

    print(f"Train accuracy: {trainAcc:.4f}")
    print(f"Test accuracy: {testAcc:.4f}")
    

if __name__ == "__main__":
    main()
