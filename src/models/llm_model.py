import logging
import cohere
from src.config import COHERE_API_KEY

logger = logging.getLogger(__name__)

llm = cohere.ClientV2(api_key=COHERE_API_KEY)
MODEL_NAME = "command-a-03-2025"


def generate_text(prompt, **kwargs):
    max_tokens = kwargs.get("max_tokens", 512)
    temperature = kwargs.get("temperature", 0.7)

    try:
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

        # Ensure the response contains text
        if (
            response.message is None
            or not response.message.content
            or len(response.message.content) == 0
        ):
            logger.warning("Cohere returned an empty response.")
            return ""

        return response.message.content[0].text.strip()

    except cohere.UnprocessableEntityError as e:
        logger.error(f"Cohere 422 Error: {e}")
        return ""

    except cohere.ApiError as e:
        logger.error(f"Cohere API Error: {e}")
        return ""

    except Exception as e:
        logger.exception(f"Unexpected error while calling Cohere: {e}")
        return ""
