def build_prompt(
    intent,
    user_message,
    profile,
    history,
    retrieved_docs=None,
    curriculum_context=None,
    bloom_level=None,
    differentiation=None,
    lesson_structure=None
):

    # -------------------------
    # Extract structured profile layers
    # -------------------------

    identity = profile.get("identity", {})
    teaching_context = profile.get("teaching_context", {})
    learner_context = profile.get("learner_context", {})
    pedagogy = profile.get("pedagogy", {})

    # -------------------------
    # Conversation history
    # -------------------------

    conversation = "\n".join(
        [f"{x['role']}: {x['content']}" for x in history]
    )

    # -------------------------
    # Structured Teacher Block
    # -------------------------

    teacher_block = f"""

TEACHER PROFILE:

Identity:
- Name: {identity.get("name")}
- School: {identity.get("school")}
- Location: {identity.get("location")}

Teaching Context:
- Curriculum: {teaching_context.get("curriculum")}
- Phase: {teaching_context.get("phase")}
- Grades: {teaching_context.get("grades")}
- Subjects: {teaching_context.get("subjects")}
- School Type: {teaching_context.get("school_type")}
- Class Size: {teaching_context.get("class_size")}
- Experience Level: {teaching_context.get("experience_level")}
- Resource Level: {teaching_context.get("resource_level")}
- Curriculum Familiarity: {teaching_context.get("curriculum_familiarity")}

Learner Context:
- Performance Level: {learner_context.get("performance_level")}
- Common Challenges: {learner_context.get("common_challenges")}
- Special Needs: {learner_context.get("special_needs")}

Pedagogy Preferences:
- Teaching Style: {pedagogy.get("teaching_style")}
- Preferred Models: {pedagogy.get("preferred_models")}
- Assessment Focus: {pedagogy.get("assessment_focus")}
"""

    # -------------------------
    # System Prompt Base
    # -------------------------

    system_prompt = f"""

You are mentorED,
a CAPS-aligned intelligent teaching assistant for South African educators.

{teacher_block}

RULES:

- Be pedagogically accurate
- Use Bloom's taxonomy appropriately
- Apply CAPS curriculum standards
- Support differentiated instruction
- Adapt to teacher context (class size, experience, resources)
"""

    # -------------------------
    # Intent-specific instructions
    # -------------------------

    if intent == "lesson_plan":

        system_prompt += """

Generate a structured lesson plan including:
- Objectives
- 5E lesson phases
- Activities
- Assessment
- Differentiation
"""

    elif intent == "assessment":

        system_prompt += """

Generate an assessment with:
- Mixed cognitive levels
- Memo/answers
- CAPS alignment
- Clear instructions
"""

    elif intent == "objectives":

        system_prompt += """

Generate SMART learning objectives using Bloom's taxonomy.
Ensure measurable and curriculum-aligned outcomes.
"""

    elif intent == "differentiation":

        system_prompt += """

Generate differentiated instruction for:
- Struggling learners
- Average learners
- Advanced learners
- Language support learners
"""

    # -------------------------
    # Inject external context
    # -------------------------

    retrieval_context = ""
    if retrieved_docs:
        retrieval_context = f"\nRetrieved Knowledge:\n{retrieved_docs}"

    curriculum_block = ""
    if curriculum_context:
        curriculum_block = f"\nCurriculum Context:\n{curriculum_context}"

    pedagogy_block = f"""

PEDAGOGY SETTINGS:
- Bloom Level: {bloom_level}
- Differentiation: {differentiation}
- Lesson Structure: {lesson_structure}
"""

    # -------------------------
    # Final Prompt Assembly
    # -------------------------

    prompt = f"""

{system_prompt}

{curriculum_block}

{pedagogy_block}

{retrieval_context}

Conversation:
{conversation}

User Request:
{user_message}

Intent:
{intent}
"""

    return prompt