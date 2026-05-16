from ai.llm import generate_response

def generate_differentiation(
    topic,
    profile=None,
    curriculum_context=None,
    retrieved_docs=None,
    bloom_level=None,
    differentiation=None,
    lesson_structure=None
):

    prompt = f"""

You are a CAPS-aligned inclusive education specialist.

Design learner differentiation strategies for a South African classroom.

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

PEDAGOGY CONTEXT:

Target Bloom Level:
{bloom_level}

Lesson Structure:
{lesson_structure}

---

INSTRUCTION:

Create differentiated instruction strategies for:

1. Struggling learners
2. Average learners
3. High-achieving learners
4. Language support learners (ESL/EAL)

---

REQUIREMENTS:

- Must be practical for classroom use
- Must support mixed-ability classrooms
- Must align with CAPS expectations
- Must include scaffolding techniques
- Must include extension activities for advanced learners
"""

    return generate_response(prompt)