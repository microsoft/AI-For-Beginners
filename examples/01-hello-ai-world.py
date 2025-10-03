"""
Hello AI World - Your First AI Program
=======================================

This is a simple pattern recognition example that demonstrates core AI concepts:
- Learning from data
- Making predictions
- Understanding patterns

What this program does:
- Learns a simple mathematical pattern (y = 2x)
- Uses that pattern to make predictions
- No complex libraries needed - just pure Python!

Perfect for understanding AI basics before diving into neural networks.
"""

import random

class SimpleAILearner:
    """
    A very simple AI that learns linear relationships.
    This demonstrates the fundamental concept of AI: learning from data.
    """
    
    def __init__(self):
        # The "weight" is what our AI learns
        # It starts with a random guess
        self.weight = random.uniform(0, 5)
        self.learning_rate = 0.01  # How fast our AI learns
        
    def predict(self, x):
        """
        Make a prediction based on what we've learned.
        
        Args:
            x: Input value
            
        Returns:
            Predicted output
        """
        return self.weight * x
    
    def train(self, training_data, epochs=100):
        """
        Train the AI to learn the pattern in the data.
        
        Args:
            training_data: List of (input, output) pairs
            epochs: Number of times to go through all the data
        """
        print("🎓 Training started...")
        print(f"Initial guess for weight: {self.weight:.2f}")
        
        for epoch in range(epochs):
            total_error = 0
            
            # Learn from each example
            for x, y_actual in training_data:
                # Make a prediction
                y_predicted = self.predict(x)
                
                # Calculate error (how wrong we were)
                error = y_actual - y_predicted
                total_error += abs(error)
                
                # Update our weight to reduce error (this is learning!)
                self.weight += self.learning_rate * error * x
            
            # Print progress every 20 epochs
            if (epoch + 1) % 20 == 0:
                avg_error = total_error / len(training_data)
                print(f"Epoch {epoch + 1}/{epochs} - Average error: {avg_error:.4f} - Weight: {self.weight:.2f}")
        
        print(f"✅ Training complete! Final weight: {self.weight:.2f}")


def main():
    """
    Main function - Let's teach our AI!
    """
    print("=" * 60)
    print("Welcome to Hello AI World!")
    print("=" * 60)
    print()
    print("Today, we'll teach an AI to learn a simple pattern:")
    print("Given x, predict y where y = 2x")
    print()
    
    # Step 1: Create training data
    # The pattern we want the AI to learn: y = 2 * x
    print("📊 Creating training data...")
    training_data = [
        (1, 2),    # When x=1, y should be 2
        (2, 4),    # When x=2, y should be 4
        (3, 6),    # When x=3, y should be 6
        (4, 8),    # When x=4, y should be 8
        (5, 10),   # When x=5, y should be 10
    ]
    print(f"Training examples: {training_data}")
    print()
    
    # Step 2: Create and train our AI
    ai = SimpleAILearner()
    ai.train(training_data, epochs=100)
    print()
    
    # Step 3: Test our AI with new data
    print("🧪 Testing our AI with new inputs...")
    print("-" * 60)
    test_inputs = [6, 7, 10, 15]
    
    for x in test_inputs:
        prediction = ai.predict(x)
        actual = 2 * x  # The true answer
        print(f"Input: {x:2d} | Prediction: {prediction:6.2f} | Actual: {actual:6.2f} | Difference: {abs(prediction - actual):.2f}")
    
    print("-" * 60)
    print()
    
    # Explanation
    print("💡 What just happened?")
    print("1. We gave the AI examples of the pattern (y = 2x)")
    print("2. The AI learned by adjusting its 'weight' to minimize errors")
    print("3. After training, it can predict outputs for new inputs!")
    print()
    print("🎉 Congratulations! You just trained your first AI!")
    print()
    print("🚀 Next steps:")
    print("   - Try changing the training data to learn different patterns")
    print("   - Experiment with the learning_rate (line 29)")
    print("   - Modify epochs to see how training time affects accuracy")
    print()


if __name__ == "__main__":
    # This runs when you execute the script
    main()
