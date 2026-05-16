def detect_intent(message):


    message = message.lower()

    if "lesson plan" in message:
        return "lesson_plan"

    if "assessment" in message:
        return "assessment"

    if "objective" in message:
        return "objectives"

    if "differentiat" in message:
        return "differentiation"

    if "teach" in message:
        return "teaching_strategy"

    return "general"
