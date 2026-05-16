VALID_SUBJECTS = [
"Mathematics",
"Physical Sciences",
"Life Sciences",
"CAT",
"IT",
"English",
"Geography",
"History"
]

def validate_subjects(subjects):


    valid = []

    for subject in subjects:

        if subject in VALID_SUBJECTS:
            valid.append(subject)

    return valid

