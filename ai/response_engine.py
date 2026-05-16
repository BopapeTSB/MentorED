from ai.router import detect_intent
from ai.prompt_builder import build_prompt
from ai.llm import generate_response

#from rag.retriever import retrieve_documents
from generators.lesson_plan_generator import generate_lesson_plan
from generators.assessment_generator import generate_assessment
from generators.objectives_generator import generate_objectives
from generators.differentiation_generator import generate_differentiation
from curriculum_engine.curriculum_api import (
    get_curriculum_context
)

from pedagogy_engine.pedagogy_decider import (
    select_bloom_level,
    select_differentiation,
    select_lesson_structure
)


def process_message(user_message, profile, history):

    # -------------------------
    # Intent Detection
    # -------------------------

    intent = detect_intent(user_message)

    # -------------------------
    # RAG Retrieval
    # -------------------------

    '''retrieved_docs = retrieve_documents(
        user_message
    )'''
    
    retrieved_docs = []
    # -------------------------
    # Curriculum Context
    # -------------------------

    curriculum_context = get_curriculum_context(
        user_message
    )

    # -------------------------
    # Grade Extraction
    # -------------------------

    grade = profile["teaching_context"]["grades"]

    grade = grade[0] if grade else "Grade 8"

    # -------------------------
    # Pedagogy Decisions
    # -------------------------

    bloom_level = select_bloom_level(
        intent,
        grade,
        user_message
    )

    differentiation = select_differentiation(
        grade
    )

    lesson_structure = select_lesson_structure(
        intent
    )

    # -------------------------
# Specialized Generator Routing
# -------------------------

    if intent == "lesson_plan":

        return generate_lesson_plan(
            topic=user_message,
            profile=profile,
            curriculum_context=curriculum_context,
            retrieved_docs=retrieved_docs,
            bloom_level=bloom_level,
            differentiation=differentiation,
            lesson_structure=lesson_structure
    )


    if intent == "assessment":

        return generate_assessment(
            topic=user_message,
            profile=profile,
            curriculum_context=curriculum_context,
            retrieved_docs=retrieved_docs,
            bloom_level=bloom_level,
            differentiation=differentiation,
            lesson_structure=lesson_structure
    )


    if intent == "objectives":

        return generate_objectives(
            topic=user_message,
            profile=profile,
            curriculum_context=curriculum_context,
            retrieved_docs=retrieved_docs,
            bloom_level=bloom_level,
            differentiation=differentiation,
            lesson_structure=lesson_structure
    )


    if intent == "differentiation":

        return generate_differentiation(
            topic=user_message,
            profile=profile,
            curriculum_context=curriculum_context,
            retrieved_docs=retrieved_docs,
            bloom_level=bloom_level,
            differentiation=differentiation,
            lesson_structure=lesson_structure
    )


# -------------------------
# FALLBACK (GENERAL CHAT)
# -------------------------

    prompt = build_prompt(
        intent=intent,
        user_message=user_message,
        profile=profile,
        history=history,
        retrieved_docs=retrieved_docs,
        curriculum_context=curriculum_context,
        bloom_level=bloom_level,
        differentiation=differentiation,
        lesson_structure=lesson_structure
    )

    response = generate_response(prompt)

    return responselan(
            topic=user_message,
            profile=profile,
            curriculum_context=curriculum_context,
            retrieved_docs=retrieved_docs,
            bloom_level=bloom_level,
            differentiation=differentiation,
            lesson_structure=lesson_structure
        )

    # -------------------------
    # Default Prompt Builder
    # -------------------------

    prompt = build_prompt(
        intent=intent,
        user_message=user_message,
        profile=profile,
        history=history,
        retrieved_docs=retrieved_docs,
        curriculum_context=curriculum_context,
        bloom_level=bloom_level,
        differentiation=differentiation,
        lesson_structure=lesson_structure
    )

    # -------------------------
    # LLM Response
    # -------------------------

    response = generate_response(prompt)

    return response
