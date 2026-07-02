"""
Classifier service - thin wrapper around the classifier pipeline.
"""

from app.core.classifier_pipeline import classify_query

def classify(query):
    return classify_query(query)
