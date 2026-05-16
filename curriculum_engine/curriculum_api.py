from curriculum_engine.subject_detector import detect_subject
from curriculum_engine.curriculum_retriever import retrieve_curriculum

def get_curriculum_context(message):

    subject = detect_subject(message)

    if not subject:
        return "No subject detected."

    curriculum = retrieve_curriculum(subject)

    return curriculum

