from ai.llm import generate_response

def generate_objectives(
    topic,
    profile=None,
    curriculum_context=None,
    retrieved_docs=None,
    bloom_level=None,
    differentiation=None,
    lesson_structure=None
):

    prompt = f"""

You are a CAPS-aligned curriculum specialist for South African education.

Generate high-quality SMART learning objectives.

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

PEDAGOGY GUIDANCE:

Target Bloom Level:
{bloom_level}

Differentiation Notes:
{differentiation}

Lesson Structure Context:
{lesson_structure}

---

REQUIREMENTS:

- Write 3–5 SMART learning objectives
- Ensure alignment with CAPS curriculum
- Ensure objectives match Bloom's taxonomy level
- Make objectives measurable and learner-centred
- Ensure progression from simple → complex thinking
"""

    return generate_response(prompt)