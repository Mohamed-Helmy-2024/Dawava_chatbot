"""
Classifier service - thin wrapper around the classifier pipeline.
"""

from src.core.classifier_pipeline import classify_query

def classify(query):
    return classify_query(query)
