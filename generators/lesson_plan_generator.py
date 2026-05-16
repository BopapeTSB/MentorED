from ai.llm import generate_response
from pedagogy_engine.lesson_structures import FIVE_E
from generators.objectives_generator import (
    generate_objectives
    )

def generate_lesson_plan(
    topic,
    profile=None,
    curriculum_context=None,
    retrieved_docs=None,
    bloom_level=None,
    differentiation=None,
    lesson_structure=None
):

    prompt = f"""

You are a CAPS-aligned expert South African educator.

Create a detailed lesson plan.

---

TOPIC:
{topic}

---

TEACHER PROFILE:
{profile}

---

CURRICULUM CONTEXT (CAPS):
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

Lesson Structure:
{lesson_structure}

---

REQUIREMENTS:

- Objectives aligned to CAPS
- Structured 5E lesson flow
- Appropriate cognitive level (Bloom)
- Clear learner differentiation
- Assessment included
"""

    return generate_response(prompt)