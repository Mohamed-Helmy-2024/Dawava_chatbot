docker rm -f chatbot


docker run -d -p 8000:8000 --name chatbot dawava-chatbot-api

docker stop chatbot

docker images

docker build -t dawava-chatbot-api .


```python
import cohere
from app.config import COHERE_API_KEY

llm = cohere.ClientV2(api_key=COHERE_API_KEY)
MODEL_NAME = "command-a-03-2025"

def generate_text(prompt, **kwargs):
    max_tokens = kwargs.get("max_tokens", 512)
    temperature = kwargs.get("temperature", 0.7)

    response = llm.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )

    return response.message.content[0].text.strip()
```
