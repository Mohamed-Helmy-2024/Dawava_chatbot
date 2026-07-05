"""
Memory pipeline.

Builds a conversation summary from the client-provided history.
The client still sends the full conversation, but instead of returning
the last N messages, this module returns an LLM-generated summary.
"""

from src.config import MEMORY_BUFFER_LIMIT
from langchain.memory import ConversationSummaryBufferMemory
from langchain_core.messages import HumanMessage, AIMessage
from langchain_cohere import ChatCohere

# Import your existing LLM instance
# Replace this import with the one already used in your project.
llm = ChatCohere(
    model="command-a-03-2025",
    temperature=0.3
)

def build_memory_buffer(history, limit=MEMORY_BUFFER_LIMIT):
    """
    Build a summarized memory buffer from conversation history.

    Args:
        history: list of
            {
                "role": "user" | "assistant",
                "content": "..."
            }

        limit:
            Maximum number of recent turns to summarize.

    Returns:
        str
            Conversation summary.
    """

    if not history:
        return "No previous memory."

    memory = ConversationSummaryBufferMemory(
        llm=llm,
        max_token_limit=1024,
        return_messages=False,
    )

    for turn in history[-limit:]:
        role = turn.get("role", "")
        content = turn.get("content", "")

        if role in ("user", "human"):
            memory.chat_memory.add_message(
                HumanMessage(content=content)
            )

        elif role in ("assistant", "ai"):
            memory.chat_memory.add_message(
                AIMessage(content=content)
            )

    summary = memory.load_memory_variables({}).get("history", "")

    return summary if summary else "No previous memory."