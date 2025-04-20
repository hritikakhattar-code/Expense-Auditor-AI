from transformers import pipeline

# Load a pre-trained model for text classification
nlp_model = pipeline("zero-shot-classification")

def analyze_description(description):
    # Update candidate labels to more relevant terms for the financial domain
    candidate_labels = ["consulting", "client", "training", "office supplies", "travel", "entertainment", "expenses"]
    
    # Perform zero-shot classification
    result = nlp_model(description, candidate_labels)
    
    # Return the label with the highest score
    return result['labels'][0], result['scores'][0]  # Returns (label, score)
