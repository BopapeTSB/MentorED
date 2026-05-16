SUBJECTS = [
"Mathematics",
"Physical Sciences",
"Life Sciences",
"Natural Sciences",
"CAT",
"IT",
"English"
]

def detect_subject(message):

    for subject in SUBJECTS:

        if subject.lower() in message.lower():
            return subject

    return None

