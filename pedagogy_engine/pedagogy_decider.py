from pedagogy_engine.differentiation import DIFFERENTIATION_STRATEGIES
from pedagogy_engine.lesson_structures import FIVE_E

def select_lesson_structure(intent):
    
    if intent == "assessment":
        return ["Explain", "Evaluate"]

    return FIVE_E

def select_differentiation(grade):
    
    if grade in ["Grade 8", "Grade 9"]:
        return [
            "visual scaffolding",
            "guided instruction"
        ]

    return DIFFERENTIATION_STRATEGIES

def select_bloom_level(intent, grade, topic):
    
    if intent == "assessment":
        return "apply"

    if intent == "lesson_plan":
        return "understand"

    if "analyze" in topic.lower():
        return "analyze"

    return "understand"
