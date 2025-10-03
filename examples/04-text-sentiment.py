"""
Simple Text Sentiment Analysis
================================

This example shows how to analyze the sentiment (emotion) of text.
It's a simplified version that teaches NLP concepts without complex libraries.

What you'll learn:
- Text preprocessing (cleaning and preparing text)
- Feature extraction (converting words to numbers)
- Sentiment classification (positive vs negative)

Use case: Determine if a movie review is positive or negative.
"""

import re
from collections import Counter

class SimpleSentimentAnalyzer:
    """
    A basic sentiment analyzer that learns from labeled examples.
    
    How it works:
    1. Learns which words appear more in positive vs negative texts
    2. Calculates a "sentiment score" for each word
    3. Uses these scores to predict sentiment of new text
    """
    
    def __init__(self):
        # Store word scores (positive words get positive scores)
        self.word_scores = {}
        # Track if we've trained
        self.is_trained = False
        
    def preprocess_text(self, text):
        """
        Clean and prepare text for analysis.
        
        Steps:
        1. Convert to lowercase
        2. Remove punctuation
        3. Split into words
        
        Args:
            text: Raw text string
            
        Returns:
            List of cleaned words
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation and special characters
        text = re.sub(r'[^a-z\s]', '', text)
        
        # Split into words
        words = text.split()
        
        # Remove very short words (like "a", "i")
        words = [w for w in words if len(w) > 2]
        
        return words
    
    def train(self, training_data):
        """
        Learn sentiment patterns from labeled examples.
        
        Args:
            training_data: List of (text, sentiment) tuples
                          where sentiment is 'positive' or 'negative'
        """
        print("🎓 Training sentiment analyzer...")
        
        # Count words in positive and negative texts
        positive_words = Counter()
        negative_words = Counter()
        
        for text, sentiment in training_data:
            words = self.preprocess_text(text)
            
            if sentiment == 'positive':
                positive_words.update(words)
            else:
                negative_words.update(words)
        
        # Calculate sentiment score for each word
        # Score > 0 means more positive, < 0 means more negative
        all_words = set(positive_words.keys()) | set(negative_words.keys())
        
        for word in all_words:
            pos_count = positive_words[word]
            neg_count = negative_words[word]
            
            # Calculate score: difference in appearances
            # Add smoothing (+1) to avoid division by zero
            total = pos_count + neg_count
            self.word_scores[word] = (pos_count - neg_count) / (total + 1)
        
        self.is_trained = True
        
        # Show some learned words
        print(f"✅ Learned sentiment for {len(self.word_scores)} words")
        print("\n📊 Most positive words:")
        sorted_words = sorted(self.word_scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:5]:
            print(f"   '{word}': {score:+.3f}")
        
        print("\n📊 Most negative words:")
        for word, score in sorted_words[-5:]:
            print(f"   '{word}': {score:+.3f}")
    
    def analyze(self, text):
        """
        Predict the sentiment of new text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Tuple of (sentiment, confidence, score)
        """
        if not self.is_trained:
            raise Exception("Please train the analyzer first!")
        
        # Preprocess text
        words = self.preprocess_text(text)
        
        # Calculate total sentiment score
        total_score = 0
        word_count = 0
        
        for word in words:
            if word in self.word_scores:
                total_score += self.word_scores[word]
                word_count += 1
        
        # Average score
        if word_count > 0:
            avg_score = total_score / word_count
        else:
            avg_score = 0
        
        # Determine sentiment and confidence
        sentiment = "positive" if avg_score > 0 else "negative"
        confidence = min(abs(avg_score) * 100, 100)  # Convert to percentage
        
        return sentiment, confidence, avg_score


def create_training_data():
    """
    Create sample training data (movie reviews with labels).
    
    In a real application, you'd have thousands of examples!
    
    Returns:
        List of (review_text, sentiment) tuples
    """
    return [
        # Positive reviews
        ("This movie was absolutely amazing and wonderful! I loved every minute.", "positive"),
        ("Brilliant performance! The acting was superb and the story captivating.", "positive"),
        ("Fantastic film! Highly recommend to everyone. Best movie of the year!", "positive"),
        ("Loved it! Great storytelling and beautiful cinematography.", "positive"),
        ("Excellent movie with outstanding performances. A must watch!", "positive"),
        ("Amazing! This film exceeded all my expectations. Truly remarkable.", "positive"),
        ("Wonderful experience! The plot was engaging and entertaining.", "positive"),
        ("Superb direction and acting! One of the best films I've seen.", "positive"),
        
        # Negative reviews
        ("Terrible movie. Waste of time and money. Very disappointed.", "negative"),
        ("Awful film! Poor acting and boring story. Would not recommend.", "negative"),
        ("Horrible! The worst movie I have ever seen. Extremely disappointing.", "negative"),
        ("Bad movie with terrible plot. Boring and predictable.", "negative"),
        ("Disappointing film. Poor execution and weak performances.", "negative"),
        ("Worst movie ever! Horrible acting and stupid storyline.", "negative"),
        ("Terrible experience. Boring and poorly made. Don't waste your time.", "negative"),
        ("Awful! Poor quality and uninteresting. Complete waste of time.", "negative"),
    ]


def main():
    """
    Main function - Let's analyze some sentiments!
    """
    print("=" * 70)
    print("Simple Text Sentiment Analysis")
    print("=" * 70)
    print("\n📚 Task: Learn to identify positive and negative movie reviews")
    print()
    
    # Step 1: Create training data
    training_data = create_training_data()
    print(f"📊 Training data: {len(training_data)} movie reviews")
    print()
    
    # Step 2: Create and train analyzer
    analyzer = SimpleSentimentAnalyzer()
    analyzer.train(training_data)
    print()
    
    # Step 3: Test on new reviews
    print("🧪 Testing on new movie reviews:")
    print("=" * 70)
    
    test_reviews = [
        "This movie was fantastic! I really enjoyed it.",
        "Boring and terrible. Not worth watching.",
        "Amazing cinematography and wonderful acting!",
        "The worst film I've seen this year. Awful.",
        "Pretty good movie with some great moments.",
        "Disappointing and poorly directed.",
    ]
    
    for i, review in enumerate(test_reviews, 1):
        sentiment, confidence, score = analyzer.analyze(review)
        
        # Visual indicator
        indicator = "😊" if sentiment == "positive" else "😞"
        
        print(f"\nReview {i}:")
        print(f"  Text: \"{review}\"")
        print(f"  {indicator} Sentiment: {sentiment.upper()}")
        print(f"  📊 Confidence: {confidence:.1f}%")
        print(f"  📈 Score: {score:+.3f}")
    
    print("\n" + "=" * 70)
    
    # Interactive mode
    print("\n💬 Try it yourself! Enter your own review (or 'quit' to exit):")
    print("-" * 70)
    
    while True:
        user_input = input("\nYour review: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        
        if not user_input:
            continue
        
        try:
            sentiment, confidence, score = analyzer.analyze(user_input)
            indicator = "😊" if sentiment == "positive" else "😞"
            
            print(f"\n{indicator} Sentiment: {sentiment.upper()}")
            print(f"📊 Confidence: {confidence:.1f}%")
            print(f"📈 Score: {score:+.3f}")
        except Exception as e:
            print(f"Error: {e}")
    
    # Explanation
    print("\n💡 What just happened?")
    print("1. The analyzer learned word patterns from example reviews")
    print("2. It calculated 'sentiment scores' for words")
    print("3. For new text, it combines word scores to predict sentiment")
    print()
    print("🎉 You just built a sentiment analyzer!")
    print()
    print("🚀 Next steps:")
    print("   - Add more training examples to improve accuracy")
    print("   - Try analyzing tweets, product reviews, or comments")
    print("   - Explore more advanced NLP in lessons/5-NLP/")
    print()


if __name__ == "__main__":
    main()
