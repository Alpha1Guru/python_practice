import re
import json
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)

ATTENDANCE_FILE = "attendance.json"

def load_attendance():
    try:
        with open(ATTENDANCE_FILE, "r") as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()

def save_attendance(attendance_set):
    with open(ATTENDANCE_FILE, "w") as f:
        json.dump(list(attendance_set), f)

# Load existing attendance
attendance_list = load_attendance()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎓 Welcome to the Attendance Bot!\n\n"
        "Use /attendance to mark your attendance.\n"
        "Your matric should look like: 240591XXX"
    )

async def attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please enter your matric number (e.g., 240591XXX):")
    context.user_data["awaiting_attendance"] = True

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if context.user_data.get("awaiting_attendance"):
        pattern = r"^240591\d{3}$"
        if not re.match(pattern, text):
            await update.message.reply_text("❌ Invalid matric number format. Try: 240591123")
            return

        if text in attendance_list:
            await update.message.reply_text("✅ Attendance already marked.")
        else:
            attendance_list.add(text)
            save_attendance(attendance_list)
            await update.message.reply_text("✅ Your attendance has been marked!")

        context.user_data["awaiting_attendance"] = False
    else:
        await update.message.reply_text("❓ Unrecognized input. Use /attendance to begin.")

def main():
    bot_token = "7718408832:AAGlkAWcfLQJbuNnwa8xHUbKD4TmfhMfrZE"

    try:
        app = ApplicationBuilder().token(bot_token).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("attendance", attendance))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

        print("✅ Bot is running...")
        app.run_polling()
    except Exception as e:
        print("❌ An error occurred:", e)


if __name__ == "__main__":
    main()
