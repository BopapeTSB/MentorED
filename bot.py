from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    filters,
    ContextTypes,
    CommandHandler
)

import json

from config_folder.settings import TELEGRAM_BOT_TOKEN

from profile_engine.profile_manager import ProfileManager
from profile_engine.validators import validate_subjects

from memory.conversation_memory import (
    get_history,
    add_message
)

from ai.response_engine import process_message


# =========================================================
# INIT
# =========================================================

profile_manager = ProfileManager()


# =========================================================
# PROFILE COMMANDS
# =========================================================

async def show_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Display the current user profile as JSON."""

    profile = profile_manager.get_profile()

    await update.message.reply_text(
        json.dumps(profile, indent=2)
    )


async def reset_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Reset the user's stored profile."""

    user_id = str(update.message.chat_id)

    profile_manager.reset_profile(user_id)

    await update.message.reply_text(
        "Profile reset."
    )
async def set_class_size(update: Update, context: ContextTypes.DEFAULT_TYPE):

    value = context.args[0] if context.args else None

    if not value:
        await update.message.reply_text("Usage: /set_class_size small|medium|large")
        return

    profile_manager.set_field(
        "teaching_context.class_size",
        value
    )

    await update.message.reply_text(f"Class size updated to {value}")
    
    
async def set_experience(update: Update, context: ContextTypes.DEFAULT_TYPE):

    value = context.args[0] if context.args else None

    if not value:
        await update.message.reply_text("Usage: /set_experience beginner|intermediate|expert")
        return

    profile_manager.set_field(
        "teaching_context.experience_level",
        value
    )

    await update.message.reply_text(f"Experience level set to {value}")
    
async def add_subject(update: Update, context: ContextTypes.DEFAULT_TYPE):

    value = " ".join(context.args)

    if not value:
        await update.message.reply_text("Usage: /add_subject Mathematics")
        return

    profile_manager.add_to_list(
        "teaching_context.subjects",
        value
    )

    await update.message.reply_text(f"Added subject: {value}")
    
    
async def set_grade(update: Update, context: ContextTypes.DEFAULT_TYPE):

    value = context.args[0] if context.args else None

    if not value:
        await update.message.reply_text("Usage: /set_grade 10")
        return

    profile_manager.set_field(
        "teaching_context.grades",
        [value]
    )

    await update.message.reply_text(f"Grade set to {value}")

# =========================================================
# SET SUBJECTS COMMAND
# =========================================================

async def set_subjects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Update subjects in the user's teaching profile."""

    user_id = str(update.message.chat_id)

    try:
        # Extract subjects from command arguments
        subjects = context.args

        # Validate subjects
        subjects = validate_subjects(subjects)

        # Update profile
        profile_manager.update_profile(
            user_id,
            {
                "teaching_context": {
                    "subjects": subjects
                }
            }
        )

        await update.message.reply_text(
            f"Subjects updated: {subjects}"
        )

    except Exception as e:
        await update.message.reply_text(
            f"Error: {e}"
        )


# =========================================================
# MAIN MESSAGE HANDLER
# =========================================================

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all non-command user messages."""

    user_id = str(update.message.chat_id)
    user_message = update.message.text

    # -------------------------
    # LOAD PROFILE
    # -------------------------
    profile = profile_manager.get_profile(user_id)

    # -------------------------
    # MEMORY SYSTEM
    # -------------------------
    add_message(user_id, "user", user_message)
    history = get_history(user_id)

    # -------------------------
    # AI RESPONSE GENERATION
    # -------------------------
    response = process_message(
        user_message=user_message,
        profile=profile,
        history=history
    )

    add_message(user_id, "assistant", response)

    # -------------------------
    # SEND RESPONSE (HANDLE LONG TEXT)
    # -------------------------
    MAX_LENGTH = 4000

    for i in range(0, len(response), MAX_LENGTH):
        chunk = response[i:i + MAX_LENGTH]
        await update.message.reply_text(chunk)


# =========================================================
# BOT STARTUP
# =========================================================

app = ApplicationBuilder().token(
    TELEGRAM_BOT_TOKEN
).build()

# Command handlers
app.add_handler(CommandHandler("profile", show_profile))
app.add_handler(CommandHandler("reset", reset_profile))
app.add_handler(CommandHandler("subjects", set_subjects))
app.add_handler(CommandHandler("set_class_size", set_class_size))
app.add_handler(CommandHandler("set_experience", set_experience))
app.add_handler(CommandHandler("add_subject", add_subject))
app.add_handler(CommandHandler("set_grade", set_grade))

# Message handler (non-command text)
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_message
    )
)

print("Bot running...")

app.run_polling(drop_pending_updates=True)
