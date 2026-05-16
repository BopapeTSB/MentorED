from ai.llm import generate_response

def generate_assessment(
    topic,
    profile=None,
    curriculum_context=None,
    retrieved_docs=None,
    bloom_level=None,
    differentiation=None,
    lesson_structure=None
):

    prompt = f"""

You are a CAPS-aligned assessment designer for South African schools.

Create a high-quality learner assessment.

---

TOPIC:
{topic}

---

CURRICULUM CONTEXT:
{curriculum_context}

---

RETRIEVED KNOWLEDGE:
{retrieved_docs}

---

PEDAGOGY SETTINGS:

Bloom Level:
{bloom_level}

Differentiation:
{differentiation}

Lesson Structure Context:
{lesson_structure}

---

REQUIREMENTS:

- Include 4–6 assessment questions
- Vary cognitive levels (Bloom)
- Include memo/answers
- Ensure CAPS alignment
- Include at least one real-world application question
"""

    return generate_response(prompt)