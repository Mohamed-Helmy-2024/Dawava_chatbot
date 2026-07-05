import cohere
from src.config import COHERE_API_KEY

client = cohere.ClientV2(api_key=COHERE_API_KEY)

EMBEDDING_MODEL = "embed-v4.0"

def get_embedding(text):
    response = client.embed(
        model=EMBEDDING_MODEL,
        texts=[text],
        input_type="search_document",
        embedding_types=["float"],
    )

    return response.embeddings.float[0]