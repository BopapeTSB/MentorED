user_memory = {}

def get_history(user_id):


    if user_id not in user_memory:
        user_memory[user_id] = []

    return user_memory[user_id]


def add_message(user_id, role, content):


    history = get_history(user_id)

    history.append({
        "role": role,
        "content": content
    })

    user_memory[user_id] = history[-10:]

