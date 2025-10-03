"""
Simple Neural Network from Scratch
===================================

This example builds a basic neural network without using any ML frameworks.
It helps you understand what's happening "under the hood" in neural networks.

What you'll learn:
- How neurons work
- Forward propagation (making predictions)
- Backward propagation (learning from mistakes)
- The sigmoid activation function

Use case: Learn to classify points as "above" or "below" a line.
"""

import random
import math

def sigmoid(x):
    """
    Sigmoid activation function: converts any value to a number between 0 and 1.
    
    This is like asking "how confident are we?" 
    - Values close to 1 mean "very confident YES"
    - Values close to 0 mean "very confident NO"
    - Values around 0.5 mean "not sure"
    
    Args:
        x: Input value
        
    Returns:
        Value between 0 and 1
    """
    # Prevent overflow for very large/small numbers
    if x > 100:
        return 1.0
    if x < -100:
        return 0.0
    return 1 / (1 + math.exp(-x))


def sigmoid_derivative(x):
    """
    Derivative of sigmoid function - needed for learning.
    This tells us how much to adjust our weights.
    
    Args:
        x: Sigmoid output value
        
    Returns:
        Derivative value
    """
    return x * (1 - x)


class SimpleNeuron:
    """
    A single artificial neuron - the building block of neural networks.
    
    Think of it as a tiny decision maker that:
    1. Takes inputs (like features of data)
    2. Multiplies them by learned weights
    3. Adds them up with a bias
    4. Applies an activation function
    5. Outputs a prediction
    """
    
    def __init__(self, num_inputs):
        """
        Initialize the neuron with random weights.
        
        Args:
            num_inputs: Number of input values this neuron will receive
        """
        # Each input gets a weight (how important is this input?)
        self.weights = [random.uniform(-1, 1) for _ in range(num_inputs)]
        # Bias helps adjust the output
        self.bias = random.uniform(-1, 1)
        # Store the last output for learning
        self.output = 0
        
    def feedforward(self, inputs):
        """
        Calculate the neuron's output (prediction).
        This is called "forward propagation".
        
        Args:
            inputs: List of input values
            
        Returns:
            Neuron's output (between 0 and 1)
        """
        # Step 1: Multiply each input by its weight and sum them
        total = sum(w * x for w, x in zip(self.weights, inputs))
        
        # Step 2: Add bias
        total += self.bias
        
        # Step 3: Apply activation function (sigmoid)
        self.output = sigmoid(total)
        
        return self.output
    
    def train(self, inputs, target, learning_rate=0.1):
        """
        Teach the neuron to improve its predictions.
        This is called "backpropagation".
        
        Args:
            inputs: The input values
            target: What the output should have been
            learning_rate: How much to adjust weights
        """
        # Calculate error
        error = target - self.output
        
        # Calculate adjustment amount using derivative
        delta = error * sigmoid_derivative(self.output)
        
        # Update weights
        for i in range(len(self.weights)):
            self.weights[i] += learning_rate * delta * inputs[i]
        
        # Update bias
        self.bias += learning_rate * delta
        
        return abs(error)


def generate_training_data(num_samples=100):
    """
    Generate sample data for training.
    
    Task: Classify points as above (1) or below (0) the line y = x.
    
    Args:
        num_samples: How many training examples to create
        
    Returns:
        List of (inputs, target) tuples
    """
    data = []
    for _ in range(num_samples):
        # Random point in 2D space (x, y coordinates)
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        
        # Label: 1 if point is above the line y=x, 0 if below
        label = 1 if y > x else 0
        
        data.append(([x, y], label))
    
    return data


def visualize_decision(neuron, test_points):
    """
    Show how the neuron classifies different points.
    
    Args:
        neuron: Trained neuron
        test_points: List of points to test
    """
    print("\n🎯 Testing the trained neuron:")
    print("-" * 70)
    print(f"{'Point':<15} | {'Prediction':<15} | {'Actual':<15} | {'Correct?'}")
    print("-" * 70)
    
    correct = 0
    for point, actual in test_points:
        prediction = neuron.feedforward(point)
        predicted_class = 1 if prediction > 0.5 else 0
        actual_class = actual
        is_correct = "✓" if predicted_class == actual_class else "✗"
        
        if predicted_class == actual_class:
            correct += 1
        
        print(f"({point[0]:5.2f}, {point[1]:5.2f}) | {prediction:14.4f} | {actual_class:^15} | {is_correct}")
    
    print("-" * 70)
    accuracy = (correct / len(test_points)) * 100
    print(f"Accuracy: {accuracy:.1f}% ({correct}/{len(test_points)} correct)")


def main():
    """
    Main function - Build and train a neural network!
    """
    print("=" * 70)
    print("Simple Neural Network from Scratch")
    print("=" * 70)
    print("\n📚 Task: Learn to classify points as above or below the line y = x")
    print()
    
    # Step 1: Generate training data
    print("📊 Generating training data...")
    training_data = generate_training_data(num_samples=100)
    print(f"Created {len(training_data)} training examples")
    
    # Show a few examples
    print("\nExample training data:")
    for i in range(3):
        point, label = training_data[i]
        position = "above" if label == 1 else "below"
        print(f"  Point ({point[0]:.2f}, {point[1]:.2f}) is {position} the line y=x")
    
    # Step 2: Create neuron
    print("\n🧠 Creating a neuron with 2 inputs (x and y coordinates)...")
    neuron = SimpleNeuron(num_inputs=2)
    print(f"Initial weights: [{neuron.weights[0]:.3f}, {neuron.weights[1]:.3f}]")
    print(f"Initial bias: {neuron.bias:.3f}")
    
    # Step 3: Train the neuron
    print("\n🎓 Training the neuron...")
    epochs = 50
    
    for epoch in range(epochs):
        total_error = 0
        
        # Train on each example
        for inputs, target in training_data:
            neuron.feedforward(inputs)
            error = neuron.train(inputs, target, learning_rate=0.1)
            total_error += error
        
        # Show progress
        if (epoch + 1) % 10 == 0:
            avg_error = total_error / len(training_data)
            print(f"Epoch {epoch + 1}/{epochs} - Average error: {avg_error:.4f}")
    
    print("\n✅ Training complete!")
    print(f"Final weights: [{neuron.weights[0]:.3f}, {neuron.weights[1]:.3f}]")
    print(f"Final bias: {neuron.bias:.3f}")
    
    # Step 4: Test the neuron
    test_data = generate_training_data(num_samples=10)
    visualize_decision(neuron, test_data)
    
    # Explanation
    print("\n💡 What just happened?")
    print("1. The neuron started with random weights")
    print("2. It looked at 100 example points and their correct labels")
    print("3. Each time it was wrong, it adjusted its weights slightly")
    print("4. After 50 rounds, it learned to classify points correctly!")
    print()
    print("🎉 You just built a neural network from scratch!")
    print()
    print("🚀 Try this:")
    print("   - Change num_samples to train on more/fewer examples")
    print("   - Modify epochs to train for longer/shorter")
    print("   - Change learning_rate (line 185) and see what happens")
    print("   - Try different decision boundaries (modify generate_training_data)")
    print()


if __name__ == "__main__":
    main()
