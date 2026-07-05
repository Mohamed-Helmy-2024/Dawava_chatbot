"""
Prompt building.

CLASSIFIER_PROMPT and build_prompt() are taken directly from the notebook,
with the memory_summary section removed (no SQL/memory allowed, and the
diagram has no memory box).

GENERAL_PROMPT is the small, simple prompt described in the diagram for
the "general" route ("Directly send query to LLM with general system
prompt" - no retrieval needed). It did not exist as a finished template
in the notebook, so a minimal one is added here.
"""

CLASSIFIER_PROMPT = """
You are a highly accurate multilingual healthcare query classifier.

Your task is to classify the user's query into EXACTLY ONE of these categories:

1. general
2. medical
3. drug

---

## CATEGORY DEFINITIONS

1. general

Use this category for:

* Greetings
* Casual conversation
* General knowledge
* Non-medical questions
* Technology/programming/business questions
* Questions unrelated to diseases, symptoms, medications, treatment, or healthcare

---

2. medical

Use this category for:

* Symptoms
* Diseases
* Medical conditions
* Diagnosis-related questions
* Treatment plans
* Medical advice
* Lab tests
* Nutrition and health
* Pregnancy
* Mental health
* Emergency situations
* Questions involving body organs or medical interpretation

IMPORTANT:

Choose "medical" if the user discusses a health issue WITHOUT asking specifically about a medicine or drug.

---

3. drug

Use this category ONLY when the query is specifically about:

* Medicine names
* Drug usage
* Dosage
* Side effects
* Drug interactions
* Active ingredients
* Pharmacology
* Alternatives/substitutes
* Drug prices
* Manufacturers
* Barcode
* Commercial/scientific names
* Medicine categories
* Storage instructions
* Contraindications
* Similar medicines

IMPORTANT:

If a medicine name appears OR the user asks about a pharmaceutical product, prioritize "drug".

---

## CLASSIFICATION RULES

* Return ONLY one label:
  general
  medical
  drug

* Do NOT explain your answer.

* Do NOT output JSON.

* Do NOT output extra text.

* Do NOT output confidence scores.

* If the query contains both disease and medicine discussion, prioritize:
  drug > medical > general
"""


def build_classifier_prompt(memory_summary, user_query):
    """
    Exact final_prompt structure from the notebook's classify_query()
    in cell 28 (memory summary + classifier prompt + query).
    """
    return f"""
MEMORY SUMMARY

{memory_summary}

====================================================

{CLASSIFIER_PROMPT}

NOW CLASSIFY THE FOLLOWING QUERY:

{user_query}
"""


def build_prompt(query, retrieved_context, memory_summary, category):
    """
    Same RAG prompt template from the notebook's build_prompt()
    (cells 40-42), including the memory_summary section.
    """
    return f"""
You are an expert multilingual healthcare AI assistant.

MEMORY SUMMARY
--------------
{memory_summary}

RULES
------

1. Use retrieved context as the primary source.

2. If retrieved content is relevant:
   prioritize it.

3. If retrieved content is incomplete,
   weak,
   or unrelated,
   answer using your own knowledge.

4. Never mention:
   - retrieval
   - RAG
   - context quality

5. Answer only in the language of the user.

6. Be concise and accurate.

7. For medical questions:
   provide safe healthcare guidance.

8. For drug questions:
   explain:
   - usage
   - dosage if known
   - side effects
   - precautions

9. If emergency symptoms appear,
   recommend urgent medical attention.

CATEGORY
---------
{category}

QUESTION
---------
{query}

RETRIEVED CONTEXT
-----------------
{retrieved_context}
"""


def build_general_prompt(query, memory_summary = "No previous memory."):
    """
    Small, simple prompt for the 'general' route (no retrieval),
    as described in the diagram.
    """
    return f"""
You are a helpful multilingual AI assistant.

Answer the user's question naturally and concisely,
in the same language as the user.

USER QUESTION:
{query}
and 
MEMORY SUMMARY:
{memory_summary}
"""
