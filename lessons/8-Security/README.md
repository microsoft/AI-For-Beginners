# AI Security

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/45)

**AI Security** is a critical discipline that ensures the confidentiality, integrity, and availability of AI systems throughout their lifecycle. As AI becomes more prevalent in production systems, understanding and mitigating security risks is essential for building trustworthy applications.

## Why AI Security Matters

AI systems face unique security challenges that traditional software doesn't:

1. **Model Theft & IP Exposure**: Trained models represent significant intellectual property investment
2. **Adversarial Attacks**: Small perturbations to inputs can cause misclassification
3. **Data Poisoning**: Corrupted training data leads to compromised models
4. **Supply Chain Risks**: Dependencies and pre-trained models can contain vulnerabilities
5. **Privacy Leaks**: Models can memorize and expose sensitive training data

## Common AI Security Threats

### 1. Model Attacks

| Attack Type | Description | Impact |
|------------|-------------|--------|
| **Model Extraction** | Querying API to reconstruct model architecture | IP theft |
| **Model Inversion** | Inferring training data from model outputs | Privacy breach |
| **Adversarial Examples** | Crafting inputs to fool the model | Misclassification |
| **Backdoor Attacks** | Embedding hidden triggers in models | Targeted failures |

### 2. Data Attacks

| Attack Type | Description | Impact |
|------------|-------------|--------|
| **Data Poisoning** | Injecting malicious data during training | Model compromise |
| **Label Flipping** | Changing labels in training data | Biased predictions |
| **Privacy Attacks** | Extracting training data from model | Data leakage |

### 3. Infrastructure Attacks

| Attack Type | Description | Impact |
|------------|-------------|--------|
| **Dependency Vulnerabilities** | Exploiting vulnerable packages | System compromise |
| **Supply Chain Attacks** | Compromised pre-trained models | Full system compromise |
| **API Exploitation** | Bypassing API security controls | Data breach |

## Security Best Practices

### Secure Development Lifecycle

```python
# Example: Secure model loading
import hashlib
import json

def load_model_safely(model_path, expected_hash=None):
    """Load model with integrity verification."""
    # 1. Verify file integrity
    with open(model_path, 'rb') as f:
        model_bytes = f.read()
        actual_hash = hashlib.sha256(model_bytes).hexdigest()
    
    if expected_hash and actual_hash != expected_hash:
        raise ValueError("Model integrity check failed!")
    
    # 2. Load with safe deserialization
    model = safe_deserialize(model_bytes)
    return model

# Usage
model = load_model_safely(
    "model.pkl",
    expected_hash="a1b2c3d4e5f6..."
)
```

### Input Validation

```python
# Example: Input validation for ML API
from pydantic import BaseModel, validator
import numpy as np

class PredictionRequest(BaseModel):
    features: list[float]
    
    @validator('features')
    def validate_features(cls, v):
        # 1. Check feature count
        if len(v) != 10:  # Expected feature count
            raise ValueError("Invalid feature count")
        
        # 2. Check for NaN/Inf
        if any(np.isnan(x) or np.isinf(x) for x in v):
            raise ValueError("Features contain NaN or Inf")
        
        # 3. Check value ranges
        if not all(-1000 <= x <= 1000 for x in v):
            raise ValueError("Features out of range")
        
        return v
```

### Secure Model Storage

```python
# Example: Encrypted model storage
from cryptography.fernet import Fernet
import pickle

class SecureModelStorage:
    def __init__(self, encryption_key):
        self.cipher = Fernet(encryption_key)
    
    def save_model(self, model, path):
        """Save model with encryption."""
        model_bytes = pickle.dumps(model)
        encrypted = self.cipher.encrypt(model_bytes)
        
        with open(path, 'wb') as f:
            f.write(encrypted)
    
    def load_model(self, path):
        """Load and decrypt model."""
        with open(path, 'rb') as f:
            encrypted = f.read()
        
        model_bytes = self.cipher.decrypt(encrypted)
        return pickle.loads(model_bytes)
```

## Supply Chain Security

### Dependency Scanning

```bash
# Example: Scan Python dependencies
pip audit  # Check for known vulnerabilities
safety check  # Alternative scanner
```

### Model Provenance

Always verify the source of pre-trained models:

```python
# Example: Model verification
import requests
import hashlib

def verify_model_download(url, expected_hash):
    """Download and verify model integrity."""
    response = requests.get(url)
    
    # Verify hash
    actual_hash = hashlib.sha256(response.content).hexdigest()
    if actual_hash != expected_hash:
        raise ValueError("Model download failed integrity check!")
    
    return response.content
```

## Adversarial Robustness

### Testing for Vulnerabilities

```python
# Example: Adversarial testing
import numpy as np

def adversarial_test(model, x, epsilon=0.1):
    """Generate adversarial example."""
    # Add small perturbation
    perturbation = epsilon * np.sign(np.random.randn(*x.shape))
    x_adversarial = x + perturbation
    
    # Test if prediction changes
    original_pred = model.predict(x.reshape(1, -1))
    adversarial_pred = model.predict(x_adversarial.reshape(1, -1))
    
    return original_pred != adversarial_pred

# Use adversarial training for defense
def adversarial_training(model, X_train, y_train, epochs=10):
    """Train model with adversarial examples."""
    for epoch in range(epochs):
        for x, y in zip(X_train, y_train):
            # Generate adversarial example
            x_adv = x + 0.1 * np.sign(np.random.randn(*x.shape))
            
            # Train on both original and adversarial
            model.fit(
                [x.reshape(1, -1), x_adv.reshape(1, -1)],
                [y, y],
                epochs=1,
                verbose=0
            )
```

## Security Tools for AI

| Tool | Purpose |
|------|---------|
| **OWASP ML Top 10** | Security risk classification |
| **MLSec** | Security benchmarks and tools |
| **Adversarial Robustness Toolbox** | Adversarial defense |
| **TensorFlow Privacy** | Differential privacy |
| **PySyft** | Secure multi-party computation |

## Real-World Case Studies

### Case 1: Model Extraction Attack
- **Scenario**: Competitor queries API to reconstruct model
- **Impact**: IP theft, competitive disadvantage
- **Defense**: Rate limiting, query monitoring, watermarks

### Case 2: Data Poisoning
- **Scenario**: Attacker injects malicious data into training pipeline
- **Impact**: Biased or compromised model
- **Defense**: Data validation, anomaly detection, secure pipelines

### Case 3: Supply Chain Attack
- **Scenario**: Malicious code in pre-trained model
- **Impact**: Full system compromise
- **Defense**: Model verification, sandboxed execution

## ✍️ Exercises

1. **Vulnerability Assessment**: Use `ml-security-scanner` to analyze a sample ML pipeline
2. **Adversarial Testing**: Create adversarial examples for a simple classifier
3. **Security Audit**: Review a sample model deployment for security issues

## Conclusion

AI Security requires a holistic approach covering the entire ML lifecycle:

1. **Data Security**: Validate and protect training data
2. **Model Security**: Verify integrity and prevent theft
3. **Infrastructure Security**: Secure deployment and APIs
4. **Monitoring**: Detect and respond to attacks

By implementing security best practices from the start, you can build AI systems that are both powerful and trustworthy.

## 🚀 Challenge

Research and implement a simple watermarking technique for ML models. How can you prove model ownership without compromising performance?

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/46)

## Review & Self Study

- [OWASP Machine Learning Security Top 10](https://owasp.org/www-project-machine-learning-security-top-10/)
- [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence)
- [Microsoft Responsible AI](https://www.microsoft.com/ai/responsible-ai)
- [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox)
